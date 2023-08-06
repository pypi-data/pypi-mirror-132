# Contributing to Docusaurus

[Docusaurus](https://docusaurus.io) is our way to hopefully help to create open source documentation easier. We currently have [multiple open source projects using it](https://docusaurus.io/showcase), with many more planned. If you're interested in contributing to Docusaurus, hopefully, this document makes the process for contributing clear.

The [Open Source Guides](https://opensource.guide/) website has a collection of resources for individuals, communities, and companies who want to learn how to run and contribute to an open source project. Contributors and people new to open source alike will find the following guides especially useful:

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Building Welcoming Communities](https://opensource.guide/building-community/)

## [Code of Conduct](https://code.fb.com/codeofconduct)

Facebook has adopted a Code of Conduct that we expect project participants to adhere to. Please read [the full text](https://code.fb.com/codeofconduct) so that you can understand what actions will and will not be tolerated.

## Get Involved

There are many ways to contribute to Docusaurus, and many of them do not involve writing any code. Here's a few ideas to get started:

- Simply start using Docusaurus. Go through the [Getting Started](https://docusaurus.io/docs/installation) guide. Does everything work as expected? If not, we're always looking for improvements. Let us know by [opening an issue](#reporting-new-issues).
- Look through the [open issues](https://github.com/facebook/docusaurus/issues). Provide workarounds, ask for clarification, or suggest labels. Help [triage issues](#triaging-issues-and-pull-requests).
- If you find an issue you would like to fix, [open a pull request](#your-first-pull-request). Issues tagged as [_Good first issue_](https://github.com/facebook/docusaurus/labels/Good%20first%20issue) are a good place to get started.
- Read through the [Docusaurus docs](https://docusaurus.io/docs/installation). If you find anything that is confusing or can be improved, you can click "Edit this page" at the bottom of most docs, which takes you to the GitHub interface to make and propose changes.
- Take a look at the [features requested](https://github.com/facebook/docusaurus/labels/feature) by others in the community and consider opening a pull request if you see something you want to work on.

Contributions are very welcome. If you think you need help planning your contribution, please ping us on Twitter at [@docusaurus](https://twitter.com/docusaurus) and let us know you are looking for a bit of help.

### Join our Discord Channel

We have the [`#contributors`](https://discord.gg/6g6ASPA) channel on [Discord](https://discord.gg/docusaurus) to discuss all things about Docusaurus development. You can also be of great help by helping other users in the help channel.

### Triaging Issues and Pull Requests

One great way you can contribute to the project without writing any code is to help triage issues and pull requests as they come in.

- Ask for more information if you believe the issue does not provide all the details required to solve it.
- Suggest [labels](https://github.com/facebook/docusaurus/labels) that can help categorize issues.
- Flag issues that are stale or that should be closed.
- Ask for test plans and review code.

## Our Development Process

Docusaurus uses [GitHub](https://github.com/facebook/docusaurus) as its source of truth. The core team will be working directly there. All changes will be public from the beginning.

All pull requests will be checked by the continuous integration system, GitHub actions. There are unit tests, end-to-end tests, performance tests, style tests, and much more.

### Branch Organization

Docusaurus has one primary branch `main` and we use feature branches with deploy previews to deliver new features with pull requests.

## Proposing a Change

If you would like to request a new feature or enhancement but are not yet thinking about opening a pull request, you can also file an issue with the [feature template](https://github.com/facebook/docusaurus/issues/new?assignees=&labels=feature%2Cneeds+triage&template=feature.yml).

If you intend to change the public API (e.g., something in `siteConfig.js`) or make any non-trivial changes to the implementation, we recommend filing an issue with the [proposal template](https://github.com/facebook/docusaurus/issues/new?assignees=&labels=proposal%2Cneeds+triage&template=proposal.yml). This lets us reach an agreement on your proposal before you put significant effort into it. These types of issues should be rare.

If you're only fixing a bug, it's fine to submit a pull request right away but we still recommend [filing an issue](https://github.com/facebook/docusaurus/issues/new?assignees=&labels=bug%2Cneeds+triage&template=bug.yml) detailing what you're fixing. This is helpful in case we don't accept that specific fix but want to keep track of the issue.

### Reporting New Issues

When [opening a new issue](https://github.com/facebook/docusaurus/issues/new/choose), always make sure to fill out the issue template. **This step is very important!** Not doing so may result in your issue not managed in a timely fashion. Don't take this personally if this happens, and feel free to open a new issue once you've gathered all the information required by the template.

- **One issue, one bug:** Please report a single bug per issue.
- **Provide reproduction steps:** List all the steps necessary to reproduce the issue. The person reading your bug report should be able to follow these steps to reproduce your issue with minimal effort.

### Bugs

We use [GitHub Issues](https://github.com/facebook/docusaurus/issues) for our public bugs. If you would like to report a problem, take a look around and see if someone already opened an issue about it. If you are certain this is a new, unreported bug, you can submit a [bug report](#reporting-new-issues).

If you have questions about using Docusaurus, contact the Docusaurus Twitter account at [@docusaurus](https://twitter.com/docusaurus), and we will do our best to answer your questions.

You can also file issues as [feature requests or enhancements](https://github.com/facebook/docusaurus/labels/feature%20request). If you see anything you'd like to be implemented, create an issue with [feature template](https://raw.githubusercontent.com/facebook/docusaurus/main/.github/ISSUE_TEMPLATE/feature.md)

### Security Bugs

Facebook has a [bounty program](https://www.facebook.com/whitehat/) for the safe disclosure of security bugs. With that in mind, please do not file public issues; go through the process outlined on that page.

## Pull Requests

### Your First Pull Request

So you have decided to contribute code back to upstream by opening a pull request. You've invested a good chunk of time, and we appreciate it. We will do our best to work with you and get the PR looked at.

Working on your first Pull Request? You can learn how from this free video series:

[**How to Contribute to an Open Source Project on GitHub**](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

We have a list of [beginner friendly issues](https://github.com/facebook/docusaurus/labels/good%20first%20issue) to help you get your feet wet in the Docusaurus codebase and familiar with our contribution process. This is a great place to get started.

### Versioned Docs

If you only want to make content changes you just need to be aware of versioned docs.

- `website/docs` - The files in here are responsible for the "next" version at https://docusaurus.io/docs/next/installation.
- `website/versioned_docs/version-X.Y.Z` - These are the docs for the X.Y.Z version at https://docusaurus.io/docs/X.Y.Z/installation.

To make a fix to the published versions you must edit the corresponding markdown file in both folders. If you only made changes in `docs`, be sure to be viewing the `next` version to see the updates (ensure there's `next` in the URL).

> Do not edit the auto-generated files within `versioned_docs/` or `versioned_sidebars/` unless you are sure it is necessary. For example, information about new features should not be documented in versioned docs. Edits made to older versions will not be propagated to newer versions of the docs.

### Installation

1. Ensure you have [Yarn](https://yarnpkg.com/) installed.
1. After cloning the repository, run `yarn install` in the root of the repository.
1. To start a development server, run `yarn workspace website start`.

### Online one-click setup for contributing

You can use Gitpod (a free, online, VS Code-like IDE) for contributing. With a single click it will launch a workspace (for Docusaurus 2) and automatically:

- clone the docusaurus repo.
- install the dependencies.
- run `yarn start`

So that you can start contributing straight away.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/facebook/docusaurus)

You can also try using the new [github.dev](https://github.dev/facebook/docusaurus) feature. While you are browsing any file, changing the domain name from `github.com` to `github.dev` will turn your browser into an online editor. You can start making changes and send pull requests right away.

### Sending a Pull Request

Small pull requests are much easier to review and more likely to get merged. Make sure the PR does only one thing, otherwise please split it. It is recommended to follow this [commit message style](#semantic-commit-messages).

Please make sure the following is done when submitting a pull request:

1. Fork [the repository](https://github.com/facebook/docusaurus) and create your branch from `main`.
1. Add the [copyright notice](#copyright-header-for-source-code) notice to the top of any code new files you've added.
1. Describe your [**test plan**](#test-plan) in your pull request description. Make sure to [test your changes](https://github.com/facebook/docusaurus/blob/main/admin/testing-changes-on-Docusaurus-itself.md)!
1. Make sure your code lints (`yarn prettier && yarn lint`).
1. Make sure your Jest tests pass (`yarn test`).
1. If you haven't already, [sign the CLA](https://code.facebook.com/cla).

All pull requests should be opened against the `main` branch.

#### Test Plan

A good test plan has the exact commands you ran and their output, provides screenshots or videos if the pull request changes UI.

- If you've changed APIs, update the documentation.

If you need help testing your changes locally, you can check out the doc on doing [local third party testing](https://github.com/facebook/docusaurus/blob/main/admin/local-third-party-project-testing.md).

#### Breaking Changes

When adding a new breaking change, follow this template in your pull request:

```md
### New breaking change here

- **Who does this affect**:
- **How to migrate**:
- **Why make this breaking change**:
- **Severity (number of people affected x effort)**:
```

#### Copyright Header for Source Code

Copy and paste this to the top of your new file(s):

```python
/**
 # Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
 # LICENSE file in the root directory of this source tree.
 */
```

#### Contributor License Agreement (CLA)

In order to accept your pull request, we need you to submit a CLA. You only need to do this once, so if you've done this for another Facebook open source project, you're good to go. If you are submitting a pull request for the first time, the Facebook GitHub Bot will reply with a link to the CLA form. You may also [complete your CLA here](https://code.facebook.com/cla).

After you have signed the CLA, the CLA bot would automatically update the PR status. There's no need to open a new PR.

**CLAs are required for us to merge your pull request.** While we value your effort and are willing to wait for you to come back and address the reviews in case you are unavailable after sending the pull request, pull requests that are ready to merge but have CLA missing and no response from the author **will be closed within two weeks of opening**. If you have further questions about the CLA, please stay in touch with us.

If it happens that you were unavailable and your PR gets closed, feel free to reopen once it's ready! We are still happy to review it, help you complete it, and eventually merge it.

### What Happens Next?

The core Docusaurus team will be monitoring for pull requests. Do help us by keeping pull requests consistent by following the guidelines above.

## Style Guide

[Prettier](https://prettier.io) will catch most styling issues that may exist in your code. You can check the status of your code styling by simply running `yarn prettier`.

However, there are still some styles that Prettier cannot pick up.

## Semantic Commit Messages

See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional. If your change is specific to one/two packages, consider adding the scope. Scopes should be brief but recognizable, e.g. `content-docs`, `theme-classic`, `core`

The various types of commits:

- `feat`: a new API or behavior **for the end user**.
- `fix`: a bug fix **for the end user**.
- `docs`: a change to the website or other Markdown documents in our repo.
- `refactor`: a change to production code that leads to no behavior difference, e.g. splitting files, renaming internal variables, improving code style...
- `test`: adding missing tests, refactoring tests; no production code change.
- `chore`: upgrading dependencies, releasing new versions... Chores that are **regularly done** for maintenance purposes.
- `misc`: anything else that doesn't change production code, yet is not `test` or `chore`. e.g. updating GitHub actions workflow.

Do not get too stressed about PR titles, however. The maintainers will help you get them right, and we also have a PR label system that doesn't equate with the commit message types. Your code is more important than conventions!

### Example

```
feat(core): allow overriding of webpack config
^--^^----^  ^------------^
|   |       |
|   |       +-> Summary in present tense.
|   |
|   +-> The package(s) that this change affected.
|
+-------> Type: see below for the list we use.
```

Use lower case not title case!

## Code Conventions

### General

- **Most important: Look around.** Match the style you see used in the rest of the project. This includes formatting, naming files, naming things in code, naming things in documentation.
- "Attractive"
- We do have Prettier (a formatter) and ESLint (a syntax linter) to catch most stylistic problems. If you are working locally, they should automatically fix some issues during every git commit.

### Documentation

- Do not wrap lines at 80 characters - configure your editor to soft-wrap when editing documentation.

## License

By contributing to Docusaurus, you agree that your contributions will be licensed under its MIT license.
