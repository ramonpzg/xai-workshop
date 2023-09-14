# Unlocking ~the Black-Box~ ML Models


## Description

In the era of complex and powerful machine learning (ML) models, understanding the decision-making process of these models has become a challenge, and different interpretability methods can help us build trust, address bias, and ensure compliance with different standards. The Alibi Explain library offers a comprehensive toolkit for interpreting machine learning models and shedding light on their inner workings. No prior experience with the library is required, but some knowledge of machine learning is expected.

During the workshop, we will cover the fundamental concepts and techniques of interpretable machine learning, exploring various explainability methods supported by Alibi Explain. We will discuss strategies such as rule-based explanations, feature importance, and counterfactual explanations. Through hands-on exercises, participants will gain practical experience in interpreting models and understanding their predictions.

Throughout the workshop, we will emphasize real-world applications and use cases to demonstrate the relevance and importance of interpretable machine learning. We will discuss how interpretability can enable better decision-making in finance, healthcare, and retail domains. By the end of the workshop, attendees will have a good understanding of interpretable machine learning concepts and practical skills for finding an alibi for their ML models.


## Objectives

By the end of the workshop, you will be able to,
- Explain the what Explainable AI is.
- Understand the differences between interpretable and explainable machine learning.
- Pick the right model for the right problem.
- Understand how to visualize the outputs of your explanation models.


## Format
The tutorial has a setup section, three major lessons of ~50 minutes each, and 2 breaks of 10 minutes each. In addition, each of the lessons contains some allotted time for exercises that are designed to help solidify the content taught throughout the workshop.

## Audience
The target audience for this session includes analysts of all levels, developers, data scientists and machine learning engineers wanting to learn how to create different data pipelines and the appropriate infrastructure required for a data project.

## Prerequisites (P) and Good To Have's (GTH)

- **(P)** Attendees for this tutorial are expected to be familiar with Python (1 year of coding). 
- **(P)** Participants should be comfortable with loops, functions, lists comprehensions, and if-else statements.
- **(P)** Some machine learning knowledge is expected.
- **(GTH)** While it is not necessary to have any knowledge of data visualization libraries, some experience with matplotlib or seaborn would be very beneficial throughout this tutorial.
- **(P)** Participants should have at least 5 GB of free space in their computers.

## Setup

If you are on a Mac or Linux machine, the set up steps will be the same. If you are in a 
Windows machine, you can still follow along with the tutorial, but please bare in mind 
that your experience  will be a much better one if you were to download, install and use 
(preferrably) Windows Subsystem for Linux or Git Bash for the session.

You can set up the environment with mamba, conda or with virtualenv. For those who want to use 
conda/mamba, you should first make sure you have [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Micromamba](https://github.com/conda-forge/miniforge#mambaforge) installed before 
following the next steps.

#### First Step

Open up your terminal and navigate to a directory of your choosing in your computer. Once there, run the following command to get the code for the session.

```sh
 git clone https://github.com/ramonpzg/xai-worksohp.git
```

Conversely, you can click on the green `download` button at the top and donwload all 
files to your desired folder/directory. Once you download it, unzip it and move on 
to the second step.

#### Second Step

To get all dependencies, packages and everything else that would be useful in this 
tutorial, you can recreate the environment by first going into the directory for today.

```sh
cd xai-worksohp
```

Then you will need to create an environment with all of the dependencies needed for the session by running the following command.

```sh
mamba create -n xai_pydata_ams python=3.10
mamba activate xai_pydata_ams
pip install -r requirements.txt

## OR

conda create -n xai_pydata_ams python=3.10
conda activate xai_pydata_ams
pip install -r requirements.txt

## OR

python -m venv venv
source venv/bin/activate
pip install -f requirements.txt
```

#### Third Step

Open up Jupyter Lab and you should be ready to go.

```sh
code .

## OR

jupyter lab
```

Great work! Now navigate to `01_diabetes.ipynb` and open it.


## Resources

Here are a few great resources to get started with the topics covered in this workshop.

- [Explainable AI for Practitioner](https://www.oreilly.com/library/view/explainable-ai-for/9781098119126/) 
by Michael Munn and David Pitman
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) 
by Christoph Molnar
- [Interpretable Machine Learning with Python, Second Edition: Build Your Own Interpretable Models](https://www.packtpub.com/product/interpretable-machine-learning-with-python-second-edition/9781803235424) by Serg Masís