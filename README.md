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

You'll then want to create an output directory (perhaps relevant to your search query).
If you wanted to use these output files directly as data, you could write them to a `_data`
directory (for jekyll). Since I'm going to just create a separate interface in a different
subfolder, I'm going to write a script instead to process them into a collection (and ideally
in the future we can import them into a database proper instead of a static site!)
For now, let's make the `dlopen` directory.


```bash
$ mkdir dlopen
```

### 3. Run the extraction

And run the script, providing the query string (first) and the output directory (second)

```bash
$ spack python search_spack.py dlopen ./dlopen
```

⚠️ *Important: As you are running this, the `var/spack/cache` is going to fill up. Likely you want to clear it if you are running out of disk space.* ⚠️

### 4. Generate the interface

You actually have two options for the interface! A static one that can be seen on
GitHub pages, and an entire search application that uses elasticsearch for indexing.

#### Static Interface

Given you have a folder of dlopen results, you can use the [generate_interface.py](generate_interface.py)
script to do exactly that. Note that this is going to generate files in [_staging](docs/_staging) and
[_data](docs/_data). Let's first generate those files:

```bash
$ python generate_interface.py dlopen/ docs/
```

Note that there are two ways to build the interface. The first (for development) is if you need
to debug and profile to see how long things are taking. For this approach, move one letter 
at a time into the packages folder, and build incrementally:

```bash
cd docs
./build.sh
```

This is my preferred way to build so I can see if any files are taking too much time
(or if it hangs, inspect the largest file for the letter being processed). In practice
this came down to just one package that was mostly javascript. The other approach is 
(when you know that the build is reasonable to do) you can just
move all files into the `_packages` folder and build / server:

```bash
$ mv _staging/*.md _packages/
$ bundle exec jekyll build
# or
$ bundle exec jekyll serve
```

Note that building (and updating) usually takes 20-30 seconds. Be patient, grasshopper.
This static site is surprisingly powerful in that it can show packages with versions,
link you to the previous/next package, and show you tags (languages) associated with each.

#### SearchApp

The container-based interface (and instructions for building and populating the database) can
be found in [app](app).


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
