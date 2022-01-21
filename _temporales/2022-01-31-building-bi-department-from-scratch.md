---
title: 'Building a BI department from scratch (I) - Infrastructure'
excerpt: 'Exploració del futur de la llar en uns anys.'
date: 2018-02-15
permalink: /temporales/2022/01/building-bi-department-from-scratch/
tags:
  - data
categories:
  - tech
  - data
---

The main reason to write this post is to materialize my thoughts and experiences around working in data analytics
for corporate environment. 
Being specific, working in a department with highly focus on financial data, but having some degree of responsibilities 
around product, marketing, customer support and sales analytics.

In it I will try to place the ideas about technologies to be considered, guidelines on how to balance tradeoffs
and better strategic paths to follow in order to grow quickly to a stable state and deliver fast and good.


# Infrastructure: the always first challenge
The always first challenge when you don't have anything is the infrastructure.
When everything comes around starting extracting value to data that is an undesirable but unavoidable path.
Decisions taken at this stage can condition the future of the performance and success of initiatives to come.

The best way to move on is to take an iterative approach by first do quick moves that can later be iterated
from them, but being sure that those are not going to condition future processes.

From here on, we have to give for granted that our infrastructure will be hosted in the cloud.
Some of the points and guidelines that will be mentioned in this posts are also valid for
on-premise infrastructure but for sure there are better sources of knowledge around them than this one post.

From that, what to do?

## Identify main components and categorize them
In order to start taking decisions about future tasks, before it is better to understand which are those tasks,
and by that which are the technical problems we really want to solve. 
Those decisions will be taken by you alone with with the help of your first hiring.

Those main tasks are around solving the next questions:
* How to consume data from? Without no data there is no data tasks. And without no data tasks there is no need for data
professionals.
* How to store the data? When we consume the data we have to place it elsewhere. The decision on where to store
the data will depend on different factors that we will explore in next steps.
* How to process data? We need to compute KPIs, do statistics, understand behaviours and identify patterns in the data.
We need a way to perform all these transformations on them efficiently and easily.
* How to give output to this data? Without any purpose for processing or any end-consumer of the data, all the job
of consuming and processing makes no sense.

Those points translate to different technical concepts as:
* Cloud provider: mainly which cloud provider to select. That decision probably will not be in your initial scope as
company for sure has some cloud to start with.
There are companies that approach that topic with a multi-cloud solution but it is always recommended to start with
only one of them.
Cloud providers include easy to use services that can help to ease some of the tasks that you need to have done.
the criteria on how to select a cloud can be discuss more in this same article in the future.
* VPC and security: all the data and operations that you do must need to be secured somehow and being able to control
the traffic to our data and basic services.
* Services to move the data: that can vary from proprietary tools, services provided by your cloud provider or
code launched in some computational resource.
* Data lake: it is where to store data cheaply but being able to retrieve it easily and start using it.
* Data Warehouse: a place to store but also process and make data highly available for analytical purposes.
* Reporting: way to visualize your data and help other teams to share the insights of the data.

And also in addition to these others:
* Access layer: a way to deliver raw data to the external data consumers.
* Down-streaming pipelines (or export pipelines): a way to export data to the operational systems in order to
make the data useful as soon as possible in the systems where process are taking place.
* Orchestration layer: we need a way to run the tasks in the proper sequence according to their inter-dependencies, 
and in the right time.


# Main criteria points to decide infrastructure
There are no good or bad decisions or systems per se.
Those questions can not be answered without understanding the context,
understanding then the tradeoffs needed to be taken,
creating a proper prioritization on what it is needed to have or what we can afford to not have, 
and do proper balances around all of them.

All of that is a matching problem.
You need to match infrastructure and tools to needs that your company has.
That involves knowing in depth what each tool and service can offer to you,
which are the limitations of these tools,
and how much this set of specifications cover your needs.


## Data consumer and data user type
Another important thing is to know the **context** in which this environment will be placed.
Most importantly the context about the professionals involved around data and their tasks.

We always have to distinguish data consumers between the ones that have technical abilities to process
and to contribute to the whole data ecosystem and the ones that are not technical enough but they need to consume
this data.

Depending on which is the proportion of people around, working with that you can focus on different strategies,
or either focus on giving data access to as many data as possible in the company in one place,
or either trying to give quality integrated data that can act to a single source of truth.
Most of the case will be a compromise between the two extremes.

One extreme will put the burden on extracting value from the data to the edge data teams or data units,
the other one will put the burden in a centralized team or unit.


## Content data properties
Other topic that can become decisive in how to focus your energy is 
what is the content of the data you have to work with.
Sensitive data requires way more security and governance that non-sensitive PII data.
Compliance is a big deal in a company,
and if it is not take seriously can damage hugely its reputation or even its treasury.

Being able to control what your data is used for is always a plus.
But when you are processing Personally Identifiable Information then it is a must.

Some tools offer quite handy usability for that purpose and can alleviate a lot of effort.


## Metadata properties
Size and structure of the data is also into the game.
Depending in how big is the data to move, we will have to choose a different type of infrastructure and architecture.
Some of the options can be directly out of the picture.











