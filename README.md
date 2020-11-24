# Demonstrating extension pack for use on the Kodexa platform

The template serves as a base for building custom extension packs to be deployed on the Kodexa Platform.

## Clone the repository, then update the project with your specific values:
* Replace all instances of demo_extension with the true name of your module:
> * environment name in environment.yml
> * module name (name of folder)
> * pythonPackage value in kodexa.yml
> * package name for the 'test-tagger' step definition in kodexa.yml
> * name and package name in setup.py
> * logger name in dummy_module.py (assuming you keep that as an example)
> * module name in tagger_test.py

* Replace all instances of demo-extension with the true name of your extension:
> * extension pack slug value in kodexa.yml

* Update setup.py author, description, email, and url values with your own information.

* Add any python packages you'll need as dependencies to the requirements.txt file.

* Change/update/remove --site option of package command that's specified in the .github/workflows/main.yml file.  More information on this setting can be found further down this README in the "Package extension for deployment" section.

> NOTE:  setup.py already includes kodexa as a dependency in 'install_requires'.  You will need to add then names of any other packages needed at runtime here, as well.


## Setting up Development Environment

To build and run this project locally, you should follow Kodexa standards.  We use Conda as our environment manager and manage our dependencies using pip (listed in requirements.txt file).

### Install Anaconda 3
Ensure you have Anaconda 3 installed - instructions are found here:

> [Installing Anaconda](https://docs.anaconda.com/anaconda/install/)

### Create local environment
Once Anaconda is installed, navigate to the root of this repository and run:

    conda env create -f environment.yml --force

This will create the conda environment (the name will be whatever you set when you were replacing values, as instructed above).  You can now activate that environment for use at command line, with Juypter notebooks, or in your preferred IDE.

### Install dependencies with pip
Activate the conda environement, then use pip to install dependencies:

> pip install -r requirements.txt

## Develop your custom actions
You can use the basic example, provided in the dummy_module.py, as a jumping off point for the creation of custom actions.  All Kodexa actions are written as classes and require 3 methods:

* __init__: this is where you will specify any parameters to that will be used throughout the class.  Parameters are not required, but if any other methods in your class require parameter values, this is where they must be specified.
* get_name:  a method that takes no parameters and returns the name of the method.
* process: the action called by the pipeline to do the actual processing of the logic.  This method always, and only, takes two parameters, document and context.

We advise that you write your action, create a test for it, and ensure it execute correctly when added as a step to a pipeline (example provided in tests/tagger_test.py) before attempting to deploy the action as part of an extension pack.

### Add action information to kodexa.yml
Once your action is ready to be deployed as part of the custom extension pack, you'll need to add it to the kodexa.yml file.  You can view the example provided for the 'test-tagger' in the kodexa.yml file.

* Within a single extension pack, action slugs are required and must be unique.
* Options:
> * Options are not required.  If your action has no options, you should list the setting as:
>    options: []
* If you do provide options, the following information should also be provide:
> * name: The name for the option (required).  Should be composed of letters and underscores.
> * required: Boolean indicating if this option is/is not required (True/False)
> * type:  The data type of the option.  Valid values are: string, number, boolean, selector, list, and regex.
> * listType: If the data type is set as list, you'll need to set the type of data to be expected in this list (string, boolean, etc.)
> * default: The default value of the option, if it's not required and not supplied
> * description: A description of the action - what it requires, what it does, and what it returns.

### Generate documentation
Once the action(s) are satisfactory, and you've specified all their details in the kodexa.yml, you should generation for the actions by running the 'document' command of the kodexa cli:
> kodexa document

This will generate markdown files documenting the actions actions described in the kodexa.yml.

## Package extension for deployment
You'll need to run the Kodexa CLI tool's 'package' command to package the code for deployment to the Kodexa Platform.  This template repository contains a workflow (.github/workflows/main.yml) where you can see this in action.  In this example. we've set the site option of the package command to deploy the packaged code (.tar.gz) to this Github repository's Github pages.  Your setup may differ.

## Kodexa CLI documentation
Additional documentation for the Kodexa CLI tool can be found on our documentation site [https://developer.kodexa.com](https://developer.kodexa.com/learning-kodexa/cli/#installing)