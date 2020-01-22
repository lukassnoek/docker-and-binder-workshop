This 1.5 hr workshop is an introduction into [Docker](https://en.wikipedia.org/wiki/Docker_(software)) and [Binder](https://jupyter.org/binder). It is primarily targeted at scientists and particularly those in (cognitive) neuroscience and psychology, but it can be followed by anyone wanting to know more about these tools in order to improve the reproducibility of their code and applications.

Importantly, this workshop is *hands-on*: you gain the most from it by actively participating. As such, you need to install some software (such as, of course, Docker, and either Python or R &mdash; see the [Prerequisites](#prerequisites-and-installation-instructions) section).

This workshop is based on the excellent, publicly available materials from [Rachael Ainsworth](https://rainsworth.github.io/osip2019-containerisation-workshop/) and [Tim Head](https://hackmd.io/CVlZEjdHQhWHDRdy53lghw#)!

## Prerequisites
As this is an introductory workshop, we don't assume any previous experience with Docker or Binder, but some basic experience with the Linux command line interface (for the Docker part) and Python or R (for the Binder part) is recommended. Moreover, as Docker only has a command line inferfance, you should be comfortable with using your operating system's terminal ("Terminal" or ITerm2 on Mac and the Command Prompt or Powershell in Windows).

## Installation instructions
To actively participate in this workshop, you need to have the following software installed:

- Docker desktop; installation instructions for [Mac & Windows](https://www.docker.com/products/docker-desktop) and [Linux](https://www.docker.com/products/docker-desktop);
- Git or [Github desktop](https://desktop.github.com/);

Lastly, you need to download the contents of the Github [repository](https://github.com/lukassnoek/docker-and-binder-workshop) associated with this workshop by clicking on the download buttons at the top (either as tar.gz or zipfile) or using `git`:

```
git clone https://lukas-snoek.com/docker-and-binder-workshop
```

Importantly, to use Docker, *you need admin (root) access* on the platform you want to run it on. You should have this on your own computer/laptop, but this is usually not the case for high-performance computing platforms (and some University-administrated computers!). While there are alternatives to Docker that do not need admin privileges (such as [Singularity](https://sylabs.io/)), we won't discuss those in this workshop in the interest of time.

## Contents
This workshop consists of roughly three parts.

* In the first part, I outline *what* Docker and Binder are and *why* you (might) want to use it;
* In the second part, you'll learn how to use *existing* Docker containers and how to create *new* ones yourself;
* In the third part, I explain what Binder is and give a short demo on how to use it.

## Slides (work-in-progress!)
To get started with the workshop (for those not at OpenMRB 2020), follow the instructions in the slides below.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQWX1FOzZFXP3Khs5OAYKM7_s4NQQbd3PAnoMM6I0CyR-zBpkLvGnFHgpBDB2rCdmFSkbIBgsIyOJe2/embed?start=true&loop=false&delayms=600000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
