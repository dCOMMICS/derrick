
  if (!("anchorName" in document.documentElement.style)) {
    import("https://unpkg.com/@oddbird/css-anchor-positioning");
  }


  if (!("anchorName" in document.documentElement.style)) {
    const { default: polyfill } = await import("https://unpkg.com/@oddbird/css-anchor-positioning/dist/css-anchor-positioning-fn.js");

    polyfill(true);
  }

if (!("anchorName" in document.documentElement.style)) {
    window.UPDATE_ANCHOR_ON_ANIMATION_FRAME = true;
    import("https://unpkg.com/@oddbird/css-anchor-positioning");
  }