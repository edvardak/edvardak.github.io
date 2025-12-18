const markdownIt = require("markdown-it");

module.exports = async function (eleventyConfig) {

  const { katex } = (await import("@mdit/plugin-katex"));

  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("style.css");
  eleventyConfig.addPassthroughCopy("slides");
  eleventyConfig.setLibrary(
  	"md,html", 
  	markdownIt().use(katex, {output: "mathml"})
  );
 eleventyConfig.addPairedShortcode("columns", function(content) {
    return `<div class="columns-container">${content}</div>`;
  });
  eleventyConfig.addPairedShortcode("column", function(content) {
    return `<div class="column">${content}</div>`;
  });
}
