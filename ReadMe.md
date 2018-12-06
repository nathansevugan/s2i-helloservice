# S2I example

## Steps
* Creating builder image (python-flask-s2i)
* Creating a python flask application based on the builder image (hello-service)

### Step 1: Install s2i utility
[Follow instructions](https://github.com/openshift/source-to-image) to install from zip or brew install s2i utilities

### Step 2: Creating the builder image

**Create an empty s2i builder project**

Use [s2i utility's command](https://github.com/openshift/source-to-image/blob/master/docs/cli.md#sti-create) create to 
create an empty project
s2i create python-flask-s2i python-flask-s2i

**Setting up the project to create a builder**

**Dockerfile**
* Fill *Dockerfile* with the base image and all the contents that you need
* Do not specify an entry point or a command since we will do that in a different file
* Provide required openshift labels in the dockerfile
* Copy the contents of the s2i/bin folder as shown below
````
COPY ./.s2i/bin/ /usr/local/s2i
````
**assemble**
 
 Assemble file accommodates various scripting languages bash or python. Make sure that you specify the scripting 
 engine at the top of the file. Example: #!/bin/bash -e .By default when the local contents are pushed to the builder image they get copied to
````
/tmp/src/
````
Copy those contents to your folder by specifying the following command in the assemble file
  
````
cp -Rf /tmp/src/. /app
````

**run**

This is where your specify the entry point to your application. Make sure that you specify the scripting 
 engine at the top of the file. Example: #!/bin/bash -e
  
**save-artifacts**
This is useful when you do incremental builds, wherein the prior dependencies are cached to avoid fetching
dependencies over and over.

**usage**
Is where you specify how to use the builder


### Step 3: Build the builder docker image
CD to python-flask-s2i folder and run *make* command. This should build the docker image. You can see by running the  *docker images* command

cmd> make


### Step 4: Using the builder image to build a new application

* CD to hello-service folder
* Execute the following s2i command to build hello-service image

````
   s2i build . python-flask-s2i hello-service
   where,
        python-flask-s2i - Builder image 
        hello-service -  New image that will be build with sources from the local folder
````

* Once done you should see the new image in the docker list

### Step 5: Running the newly built image from docker
Execute the following command to run the new image

````
docker run --rm -t -i -p 5000:5000 hello-service
````

You can access the python flask page from http://localhost:5000

