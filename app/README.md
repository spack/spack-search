# Spack Search App

This is a quick application that combines elasticsearch with postgres to
add all code files to the database in a mode, and then easily search over them.
It is derived from [django-polls-elasticsearch](https://github.com/slyapustin/django-polls-elasticsearch).

## Setup

You'll need [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)
installed on your system.

### 1. Build containers

You'll first want to build your search container.

```bash
$ docker-compose build
```

Then bring up containers:

```bash
$ docker-compose up -d
```

And ensure that they are running, without error:

```bash
$ docker-compose ps
       Name                      Command               State                       Ports                     
-------------------------------------------------------------------------------------------------------------
app_app_1             bash -c sleep 15 && python ...   Up      0.0.0.0:80->8000/tcp                          
app_elasticsearch_1   /docker-entrypoint.sh elas ...   Up      0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp
app_postgres_1        docker-entrypoint.sh postgres    Up      5432/tcp     
```

You should then be able to navigate to localhost. to see the simple interface, meaning
either at [http://localhost](http://localhost) or [http://127.0.0.1](http://127.0.0.1).
If you ever need to check logs:

```bash
$ docker-compose logs app
$ docker-compose logs nginx
$ docker-compose logs postgres
$ docker-compose logs elasticsearc
```

If you want to check that migrations ran successfully, you can look at the logs,
or shell into the container and run these commands manually.

```bash
$ docker exec -it app_app_1_bash
$ python manage.py makemigrations source
$ python manage.py migrate
$ python manage.py collectstatic --noinput
```

You can also check the status of elastic search via the RestFul API:

```bash
$ curl http://127.0.0.1:9200/
{
  "name" : "Mogul of the Mystic Mountain",
  "cluster_name" : "elasticsearch",
   ...
  "tagline" : "You Know, for Search"
}
```
```bash
$ curl http://127.0.0.1:9200/_cat/health
1613250927 21:15:27 elasticsearch yellow 1 1 5 5 0 0 5 0 - 50.0% 
```

### 2. Add Packages

You should have already cloned the repository, including all the raw package files
in the [dlopen](../dlopen) folder. If you notice in the [docker-compose.yml](docker-compose.yml),
we've actually bound this folder from the host at `/data`.

```yaml
  app:
    build: .
    depends_on:
      - postgres
      - elasticsearch
    volumes:
      - ./:/code/
      - ../dlopen:/data/     # <-------- dlopen files bound to /data
```

We can then run a management command to import these files, directing
to the `/data` folder.

```bash
$ docker exec -it app_app_1 python manage.py add_packages /data
```

Once you add packages, we need to use the haystack django integration to update our indices.
This could be further automated, but I'm walking you through it so you know what is going on.

```bash
$ python manage.py rebuild_index
WARNING: This will irreparably remove EVERYTHING from your search index in connection 'default'.
Your choices after this are to restore from backups or rebuild via the `rebuild_index` command.
Are you sure you wish to continue? [y/N] yes
Removing all documents from your index because you said so.
All documents removed.
Indexing 10 packages
GET /haystack/_mapping [status:404 request:0.001s]
Indexing 20 source files
```
```bash
$ python manage.py update_index
Indexing 10 packages
Indexing 20 source files
```

You should then be able to click packages to choose a specific one, or do a basic search in the box at the top and get some results!

⚠️ **under development** not ready for use yet! ⚠️
