function stopIframesInProgress(myBase) {
  noembed = [
    "Chrome.*Mobile",
    "Mobile.*Firefox"
  ];
  noembedRe = new RegExp(noembed.join("|"), "i");
  if (noembedRe.test(navigator.userAgent)) {
    iconSrc = myBase + "/download-pdf-icon.svg";
    iframes = document.getElementsByTagName("iframe");
    for (i = 0; i < iframes.length; ++i) {
      iframe = iframes[i];
      src = iframe.getAttribute("src");
      if (src.endsWith(".pdf")) {
        try {
          window.frames[i].stop();
        } catch (e) {
        }
        iframedoc = iframe.contentWindow.document;
        a = document.createElement("a")
        a.setAttribute("href", src);
        a.setAttribute("style", "top: 0; bottom: 0; left: 0; right: 0; position: absolute; display: flex;");
        img = iframedoc.createElement("img");
        img.setAttribute("style", "max-width: 90%; margin-left: auto; margin-right: auto; display: block;");
        img.setAttribute("src", iconSrc);
        a.appendChild(img)
        body = iframedoc.createElement("body")
        body.setAttribute("style", "margin: 0; padding: 0; background-color: rgba(0, 0, 0, 0.05);");
        body.appendChild(a);
        html = iframedoc.createElement("html");
        html.setAttribute("height", "100%");
        html.appendChild(body);
        iframe.setAttribute("srcdoc", "<html>" + html.innerHTML + "</html>");
      }
    }
  }
}

function stopAndDeferStop() {
  scripts = document.getElementsByTagName('script');
  index = scripts.length - 1;
  myScript = scripts[index];
  myBase = myScript.src.split("/").slice(0,-1).join("/");
  stopIframesInProgress(myBase);
  document.addEventListener("DOMContentLoaded", function(event) { stopIframesInProgress(myBase); });
}

stopAndDeferStop();
