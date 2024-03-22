# rice-card

A Open Graph image preview card generater written in Python.

## Feature

* Template based, can change style fastly.
* Built-in variables that let you fast combine with what you need.

## Alternative

* [Socialify](https://github.com/wei/socialify)
* [BannerBear](https://www.bannerbear.com/)

## Why this name?

Because I cooked rice today.

## Q&A

Q: Why use this technical stack? Why not built template with frontend framework?

A: There are already frontend project make a preview image, I want to try something different and let it can run headless as service.

Q: Which Pain Point you solve?

A: 1. For organization they may want to generate unified preview image style for every repository, while there isn't a workflow for those kind of batch task.
   2. GitHub's default preview image can't work correct with CJK characters.
   3. Current Socialify mainly intent for git repository, but many website (especially those built with wordpress) can't use it.
   4. You can use it preview osmcha changeset when share a link in Telegram or Discord.