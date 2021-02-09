# Spack Search

![img/spack-search.png](img/spack-search.png)

This is a small, fun project to look over spack for a query string of interest, for
example, the dlopen library. If you are interested in parsing spack packages source
code to look for content, you might find this tool useful. It's currently just a single 
script, [search_spack.py](search_spack.py), and you are invited to [open an issue](https://github.com/spack/spack-search)
or pull request to expand on that. Note that this is not related to `spack find`,
which you might be looking for instead of this repository. You can see documentation
for spack find [here](https://spack.readthedocs.io/en/latest/command_index.html#spack-find).

## Usage

### 1. Spack

Since we require spack in [search_spack.py](search_spack.py), 
you'll need to ensure that you've added the spack bin to your path before running it:

```bash
$ export PATH=$PATH:$HOME/Desktop/Code/spack/bin
```

### 2. Create output folder

You'll then want to create an output directory (perhaps relevant to your search query)

```bash
$ mkdir dlopen
```

### 3. Run the extraction

And run the script, providing the query string (first) and the output directory (second)

```bash
$ spack python search_spack.py dlopen ./dlopen
```

⚠️ *Important: As you are running this, the `var/spack/cache` is going to fill up. Likely you want to clear it if you are running out of disk space.* ⚠️

## What do we save?

Since there aren't many hits (at least for dlopen) it's easy enough to do one search
across the text, and then save the entire file for inspection.

## What can we do better?

### Visualization

At the end of a search, we will have a folder of directories, each with a json of extracted files
that contain dlopen (or the search string of interest). This isn't incredibly easy for a human to explore,
so next we can write a script that can easily parse this into a more
easy to read, human interface, and also calculate some metrics for the entire extraction.

### Multiprocessing

The skeleton is there to use multiprocessing, but since this could be scaled another way
and I was debugging, it's not being used. Feel free to change that!

# Searches

For each search, we only save a package directory if there is at least one
match result. Otherwise, we keep an entry in the .empty directory to indicate
that the package is empty (and not to check again).

 - [dlopen](dlopen)
 
Note that the current contents are just a sample, I'm still running this locally
to get the rest :)
