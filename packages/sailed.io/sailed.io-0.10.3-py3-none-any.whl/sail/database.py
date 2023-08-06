from sail import cli, util

import os, subprocess
import click
import hashlib
import pathlib
import json

from datetime import datetime

@cli.group()
def db():
	'''Import and export MySQL databases, or spawn an interactive shell'''
	pass

@db.command()
def cli():
	'''Open an interactive MySQL shell on the production host'''
	root = util.find_root()
	config = util.config()

	os.execlp('ssh', 'ssh', '-t',
		'-i', '%s/.sail/ssh.key' % root,
		'-o', 'UserKnownHostsFile="%s/.sail/known_hosts"' % root,
		'-o', 'IdentitiesOnly=yes',
		'-o', 'IdentityFile="%s/.sail/ssh.key"' % root,
		'root@%s' % config['hostname'],
		'sudo -u www-data wp --path=%s db cli' % util.remote_path('/public')
	)

@db.command(name='import')
@click.argument('path', nargs=1, required=True)
def import_cmd(path):
	'''Import a local .sql or .sql.gz file to the production MySQL database'''
	root = util.find_root()
	config = util.config()
	c = util.connection()
	remote_path = util.remote_path()

	path = pathlib.Path(path).resolve()
	if not path.exists():
		raise util.SailException('File does not exist')

	if not path.name.endswith('.sql') and not path.name.endswith('.sql.gz'):
		raise util.SailException('This does not look like a .sql or .sql.gz file')

	temp_name = '%s.%s' % (hashlib.sha256(os.urandom(32)).hexdigest()[:8], path.name)
	is_gz = path.name.endswith('.sql.gz')

	util.heading('Importing WordPress database')
	util.item('Uploading database file to production')

	args = ['-t']
	source = path
	destination = 'root@%s:%s/%s' % (config['hostname'], remote_path, temp_name)
	returncode, stdout, stderr = util.rsync(args, source, destination, default_filters=False)

	if returncode != 0:
		raise util.SailException('An error occurred in rsync. Please try again.')

	# TODO: Maybe do an atomic import which deletes tables that no longer exist
	# by doing a rename.

	util.item('Importing database into MySQL')
	cat_bin = 'zcat' if is_gz else 'cat'

	try:
		c.run('%s %s/%s | mysql -uroot "wordpress_%s"' % (cat_bin, remote_path, temp_name, config['namespace']))
	except:
		raise util.SailException('An error occurred in SSH. Please try again.')

	util.item('Cleaning up production')

	try:
		c.run('rm %s/%s' % (remote_path, temp_name))
	except:
		raise util.SailException('An error occurred in SSH. Please try again.')

	util.success('Database imported')

@db.command()
@click.option('--json', 'as_json', is_flag=True, help='Output in JSON format')
def export(as_json):
	'''Export the production database to a local .sql.gz file'''
	root = util.find_root()
	config = util.config()
	c = util.connection()
	remote_path = util.remote_path()

	if as_json:
		util.loader(suspend=True)

	backups_dir = pathlib.Path(root + '/.backups')
	backups_dir.mkdir(parents=True, exist_ok=True)
	filename = datetime.now().strftime('%Y-%m-%d-%H%M%S.sql.gz')

	if not as_json:
		util.heading('Exporting WordPress database')

	try:
		c.run('mysqldump --quick --single-transaction --default-character-set=utf8mb4 -uroot "wordpress_%s" | gzip -c9 > %s/%s' % (config['namespace'], remote_path, filename))
	except:
		raise util.SailException('An error occurred in SSH. Please try again.')

	if not as_json:
		util.item('Export completed, downloading')

	args = ['-t']
	source = 'root@%s:%s/%s' % (config['hostname'], remote_path, filename)
	destination = '%s/%s' % (backups_dir, filename)
	returncode, stdout, stderr = util.rsync(args, source, destination, default_filters=False)

	if returncode != 0:
		raise util.SailException('An error occurred in rsync. Please try again.')

	if not as_json:
		util.item('Cleaning up production')

	try:
		c.run('rm %s/%s' % (remote_path, filename))
	except:
		raise util.SailException('An error occurred in SSH. Please try again.')

	if not as_json:
		util.success('Database export saved to .backups/%s' % filename)
	else:
		click.echo(json.dumps(destination))
