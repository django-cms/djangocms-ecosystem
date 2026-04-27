# Officially endorsed django CMS packages

This repository provides a structured overview of the django CMS ecosystem, including officially supported and community-maintained packages, along with their compatibility across Django and django CMS versions.

Its goal is to help developers quickly understand:
* Which packages are available
* Their maintenance status
* Their compatibility with current supported versions

**Contributing Third-Party Packages**

We welcome contributions from the community to keep this ecosystem comprehensive and up to date.

Third-party packages can be added via a pull request, provided the existing structure of this repository is preserved.

To be included, packages must meet the following requirements:
* Support the current Django LTS release (minimum)
* Support the current django CMS LTS release (minimum)
* Demonstrate an active commitment to maintenance

Maintaining a consistent structure ensures the ecosystem remains easy to navigate and reliable for all users.

## django CMS
This chapter provides overview over the major django CMS versions, corresponding Long-Term
Support (LTS) in accordance to which Django LTS version, and actual or planned feature freezes.

### django CMS x.x
* LTS: 6.2
* feature-freeze: February 2027

### django CMS 5.1
* django: 5.2, 6.0
* python: 3.10, 3.11, 3.12, 3.13, 3.14
* feature-freeze: December 2026

### django CMS 5.0
* LTS: 5.2
* django: 4.2, 5.0, 5.1, 5.2, 6.0
* python: 3.9, 3.10, 3.11, 3.12, 3.13, 3.14
* feature-freeze: February 2025

### django CMS 4.1
* LTS: 4.2
* django: 4.2, 5.0, 5.1, 5.2
* python: 3.9, 3.10, 3.11, 3.12, 3.13
* feature-freeze: September 2023

### django CMS 3.11
* LTS: 3.2, 4.2
* django: 4.2, 5.0, 5.1
* python: 3.9, 3.10, 3.11, 3.12
* feature-freeze: September 2023

### django CMS 3.8
* LTS: 2.2
* feature-freeze: October 2020

### django CMS 3.7
* LTS: 2.2
* feature-freeze: June 2020

## CMS packages
These packages are officially endorsed by the django CMS Association.

### djangocms-admin-style
django CMS Admin Style is a Django Theme tailored to the needs of django CMS.
* django CMS: 4.1, 5.0, 5.1
* grade: production
* deprecated: 02/2026
* repo: https://github.com/django-cms/djangocms-admin-style

### djangocms-alias
Universal alias plugin for all contents that needs to be repeated within a project
* django CMS: 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-alias

### djangocms-attribute-fields
An opinionated implementation of JSONField for arbitrary HTML element attributes
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-attributes-field

### djangocms-audio
django CMS Audio is a set of plugins for django CMS. That allow you to publish audio files on your site
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-audio

### djangocms-bootstrap4
django CMS Bootstrap 4 is a plugin bundle for django CMS providing several components from the popular Bootstrap 4 framework.
djangocms-frontend offers an automatic migration
* django CMS: 3.11, 4.1, 5.0
* grade: production
* deprecated: 01/2024
* repo: https://github.com/django-cms/djangocms-bootstrap4

### djangocms-form-builder
Flexible HTML forms for your django CMS projects
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: alpha
* repo: https://github.com/django-cms/djangocms-form-builder

### djangocms-frontend
django CMS Frontend facilitates the easy creation of reusable frontend components. It supports any CSS framework.
For immediate use, it includes a comprehensive set of Bootstrap 5 components and templates
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-frontend

### djangocms-googlemap
django CMS Google Map is a set of plugins for django CMS that allow you to implement Google Map into your website.
* django CMS: 3.11
* grade: production
* repo: https://github.com/django-cms/djangocms-googlemap
* deprecated: 02/2026

### djangocms-link
Universal link plugin - allows intuitive in-text linking to all known linkable objects (starting with CMS pages).
Provides a django CMS link field and widget for developers to use in custom content elements. Compatible with
(and enabled in) djangocms-text
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-link

### djangocms-moderation
Moderation workflows for django CMS and django CMS versioning
* django CMS: 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-moderation

### djangocms-modules
Reusable user-configured components (made of existing plugins)
* django CMS: 3.11
* grade: production
* repo: https://github.com/django-cms/djangocms-modules

### djangocms-picture
django CMS Picture is a plugin for django CMS that allows you to add images on your site
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-picture

### djangocms-rest
djangocms-rest enables frontend projects to consume django CMS content through a browsable read-only, REST/JSON API
It is based on the django rest framework (DRF).
* django CMS: 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-rest

### djangocms-snippet
django CMS Snippet provides a plugin for django CMS to inject HTML, CSS or JavaScript snippets into your website
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-snippet

### djangocms-stories
django CMS blog application - Support for multilingual posts, placeholders, social network meta tags and configurable apphooks
* django CMS: 4.1, 5.0, 5.1
* grade: beta
* repo: https://github.com/django-cms/djangocms-stories

### djangocms-text
Text Plugin for django CMS using Tiptap (or any other text editor of your choice)
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: beta
* repo: https://github.com/django-cms/djangocms-text

### djangocms-text-ckeditor
Text Plugin for django CMS using CKEditor 4 (now sunset)
* django CMS: 3.11, 4.1, 5.0
* grade: production
* deprecated: 04/2025
* repo: https://github.com/django-cms/djangocms-text-ckeditor

### djangocms-text-ckeditor5
Fully-fledged CKEditor5 frontend for djangocms-text.
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: beta
* repo: https://github.com/django-cms/djangocms-text-ckeditor5

### djangocms-transfer
Import/Export (JSON) for page contents
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-transfer

### djangocms-versioning
Adds version management for django CMS pages and other packages supporting versioning
* django CMS: 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-versioning

### djangocms-video
django CMS Video is a set of plugins for django CMS that allow you to publish video content on your site
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/django-cms/djangocms-video

## Django packages
These Django packages are officially endorsed by the django CMS Association.

### django-filer
File and Image Management Application for django
* django: 4.2, 5.0, 5.1, 5.2, 6.0
* grade: production
* repo: https://github.com/django-cms/django-filer

### django-sekizai
Django Template blocks with extra functionality to manage CSS and JS
* django: 4.2, 5.0, 5.1, 5.2, 6.0
* grade: production
* repo: https://github.com/django-cms/django-sekizai

### django-classy-tags
Class-based template tags for django
* django: 4.2, 5.0, 5.1, 5.2, 6.0
* grade: production
* repo: https://github.com/django-cms/django-classy-tags

## Third-party packages
These packages are officially endorsed by the django CMS Association, but provided by third parties.
### djangocms-blog
django CMS blog application - Support for multilingual posts, placeholders, social network meta tags and configurable apphooks
* django CMS: 3.11
* grade: production
* repo: https://github.com/nephila/djangocms-blog

### djangocms-katex
Provides a django CMS plugin to render mathematical and chemical formulae written in the LaTeX languageusing.
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/fsbraun/djangocms-katex

### djangocms-maps
A universal maps plugin for django CMS, supporting all major map providers
* django CMS: 3.11
* grade: production
* repo: https://github.com/Organice/djangocms-maps

### djangocms-markdown
A markdown content plugin and model field for django CMS. Write content in Markdown using an integrated editor and have it rendered as HTML on your site.
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/fsbraun/djangocms-markdown

### djangocms-simple-admin-style
Styles the Django admin using the Django CMS theme with minimal additional CSS.
* django CMS: 3.11, 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/fsbraun/djangocms-simple-admin-style

### djangocms-timed-publishing
django CMS versioning add on, that allows for setting start and end time for an object's visibility when publishing
* django CMS: 4.1, 5.0, 5.1
* grade: production
* repo: https://github.com/fsbraun/djangocms-timed-publishing

## Third-party Django packages

## Django timelines
### 6.2
* end-of-support: 03/2030
### 6.1
* end-of-support: 12/2027
### 6.0
* end-of-support: 03/2027
### 5.2
* end-of-support: 03/2028
### 5.1
* end-of-support: 12/2025
### 5.0
* end-of-support: 03/2025
### 4.2
* end-of-support: 03/2026
### 3.2
* end-of-support: 03/2024
### 2.2
* end-of-support: 03/2022
### 1.11
* end-of-support: 03/2020
