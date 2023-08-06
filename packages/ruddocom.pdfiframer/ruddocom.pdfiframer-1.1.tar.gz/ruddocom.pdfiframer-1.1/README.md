# ruddocom.pdfiframer: correct handling of PDFs in IFRAMEs

This Plone add-on adds a bit of JavaScript that turns all served `IFRAME`s
which embed a PDF into a clickable icon the user must tap or click before
the PDF is actually embedded and rendered.  This behavior is only active
on certain mobile browsers known not to display PDFs embedded.

This not only saves you bandwidth, it also prevents a nasty behavior on
mobile devices when embedding PDFs using `IFRAME`s — instead of the PDF
being displayed, a download window pops up (yes, even when the server sends
a `Content-Disposition: inline` HTTP header).
 
Thus, visitors to your site can see the PDF onscreen with one click, and
mobile visitors can download the PDF by clicking / tapping on the icon.

Note that, by default, Plone filters `IFRAME` tags out of content types.
Use the HTML filtering control panel configuration screen to allow `IFRAME`s
to be used on your Plone site.


## Notes

We use a footer viewlet to include the JavaScript, because on mobile Fennec
or Firefox Focus, the `IFRAME` has already begun loading and the download
window pops up before the `DOMContentLoaded` event has happened.


## Setup

It's a standard Plone add-on.  Add to your Plone eggs list, buildout.


## License

The project is licensed under the GPLv2 or later at your choice.
