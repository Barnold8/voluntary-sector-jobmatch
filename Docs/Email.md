# Email -> Ideas

## Statement

This is an overview of the requirements E-Mail. The contents are similar but are not 1:1. This is because no consent was given for data collection from the stakeholder. This is just going to be some points and idea jotting to help me gather an idea on what can be done to help the stakeholder. This file is going to be more of a stream of consciousness than an actual revised document. To see a revised document on the findings here and findings externally, look at [findings.tex](findings.tex)


## Raw filtered email

    I want to prepare a database that can deliver a VOLUNTARY SECTOR JOB MATCH .

    I may mean VOLUNTARY SECTOR SKILLS match

    There is also an element of CAREER DEVELOPMENT in the **REDACTED** voluntary sector

    I don’t know what there is nationally of a similar offer.

    I wish to avoid GDPR issues with information we hold or share

    I need people to register to use the service , and have a charge for users to generate income for its management.

    It will need to describe knowledge areas, skills, previous or type of project/ work done and seeking as well as work areas considered .

    It could also have  a “ jobs available “ / skills Im looking for section

    Id like to have a reporting facility to check number of users  

## What volunteering services and companies already exist and how are they operating?
    
    This question is asked to gain some better understanding on how charities operate and what might be the most cost effective strategies. 

### [Reach volunteering](https://reachvolunteering.org.uk/)

This one is like a megaphone for smaller charities. Reach facilitates charities and organisations to post volunteering roles to the site directly for [free, (most of the time),](https://reachvolunteering.org.uk/posting-opportunity#:~:text=Reach%20Volunteering%E2%80%99s%20services,charge%20for%20volunteers) due to their funding. One major flaw of Reach is the minimum requirements for a volunteer posting, specifically the [experience required](https://reachvolunteering.org.uk/our-criteria-opportunities#:~:text=require%20three%20or%20more%20years%20professional%20experience%20in%C2%A0one%20of%20our%20skills%20areas). Reach requirees a poosting require 3 years _minimum_ for a role which defeats the point of volunteering almost entirely. 


<h4>Pros: </h4>

- Works alongside other volunteering charities to post volunteering advertisements
- Most of the time it is free to post an advertisement
- Due to the requirements for a volunteer post, its highly unlikely spam will get through

<h4>Cons: </h4>

- Limited on what volunteering roles can be posted (limited by a minimum of 3 years of experience required)

### [CharityJob](https://www.charityjob.co.uk/?source=nav)

CharityJob is a job site that also includes voluntering opportunities. CharityJob allows a volunteer poster to use their free tier which only allows a poster to keep the advert up for 90 days. They also have other tiers which depending on the funding of the charity could allow things postings being featured to relevant candidates, appear at the top of search results and be included in email alerts. For more on the price plan see [here](https://www.charityjob.co.uk/recruiters#:~:text=Compare%20your%20options)

<h4>Pros: </h4>

- Easy and free to make a posting
- Great testimonials
- Works with a lot of charities already

<h4>Cons: </h4>

- Less likely to be seen due to the mix of job roles and volunteering roles
- Less features than other sites due to paid features

### [Do It](https://www.doit.life/)

With their home page giving more information on themselves than their [about me](https://www.doit.life/about) page, its hard to say exactly what do it does, but it seems to be in the same vein as [reach volunteering](#reach-volunteering). Looking at the stakeholders website, there are volunteering job postings that originally pointed to doit, which means the stakeholder is already accustomed to them. 

<h4>Pros: </h4>

- Unlimited advertisement posting
- Free posting
- High user count
- GDPR compliant

<h4>Cons: </h4>

- Get lost in advertiser noise
- Possibility to get flagged as spam or lost in a sea of fake postings

### A look into random charities from around the UK 

In this process, I am looking into how charities in more wealthy areas **and** poorer areas operate. This is to get more of a financial idea on how these charities operate too. With this I can surmise on the technologies and practices that lower income and higher income charities operate on average. For example a higher wealth area charity _might_ use [redis](https://redis.io/) to cache user queries and have multiple on site machines to host web servers. Whereas a less wealthy area may only have a basic [static website](https://en.wikipedia.org/wiki/Static_web_page) with a link to a google form that employees at the charity sift through themselves with no automation. I am not going to state the areas of which have higher or lower wealth on average. However, I am using the [2021 cenesus map](https://www.ons.gov.uk/census/maps/choropleth/population/household-deprivation/hh-deprivation/household-is-deprived-in-one-dimension) from the [Office of national statistics](https://www.ons.gov.uk/)

#### [TogetherCo - Brighton](https://togetherco.org.uk/)

<h4> How do they get volunteers? </h4>

- Volunteer section on website
    - Has specific role postings
    - Has a form to fill out to then have a [discussion with the charity](https://togetherco.org.uk/volunteer/#:~:text=We%20will%20contact,you%20might%20have.) on whats best for you in terms of volunteering

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

#### [TogetherCo - Brighton](https://togetherco.org.uk/)

#### [TogetherCo - Brighton](https://volunteer.communityworks.org.uk/)

#### [TogetherCo - Brighton](https://www.handsonlondon.org.uk/volunteer)

#### [TogetherCo - Brighton](https://www.thekidsnetwork.org.uk/i-want-to-mentor?gad_source=1&gad_campaignid=22790719866&gbraid=0AAAAADRkgo9ZgrjOC3w8BTZU-XkR_5Yrm&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJlH0f1fgNgS3j_ExdetIzvqbD3oBxhusiLByw8EieP9HI863fcQbQaAlPtEALw_wcB)

#### [TogetherCo - Brighton](https://volunteercentrenewcastle.org.uk/)

#### [TogetherCo - Brighton](https://vast.org.uk/)

#### [bvsc - Birmingham](https://www.bvsc.org/)


## Taking the ideas head on

### I want to prepare a database that can deliver a VOLUNTARY SECTOR JOB MATCH

A database might not be the most ideal idea for this straight away unless some app, API and/or website is needed. For a small company in the volunteering sector it might be better to utilise already existing technologies to minimise costs.

#### Usage for an app

A database for an app makes perfect sense. If you require an app, to store user accounts, volunteer postings etc, you will need a database to store this information

#### Usage for a API

This would be more of something like an [API](https://en.wikipedia.org/wiki/API) that developers could use to grab local volunteer listings from your repository and deploy it to their apps and/or websites. 

#### Usage for a website

Much like the app perspective, it makes perfect sense. The same usages you would have for a databse for an app, you would have for a website too. In fact, your website and app could be pulling from the same server but using their respective technologies (like a [web browser](https://en.wikipedia.org/wiki/Web_browser), [app framework](https://developer.android.com/studio?gclsrc=aw.ds&gad_source=1&gad_campaignid=21831783765&gbraid=0AAAAAC-IOZlBp3YbgXT-JrGgb1AAgF07y&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxKEUWY1-eJuf-FFt4QEOMyA0PQYZ2OeX3fH-dCSjJoNFEm91e08zBYaAuExEALw_wcB))