const mathjaxPlugin = require("eleventy-plugin-mathjax");
const { DateTime } = require("luxon");
const markdownIt = require("markdown-it");
const markdownItAttrs = require("markdown-it-attrs");


module.exports = async function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("fonts");
  eleventyConfig.addPassthroughCopy("style.css");
  eleventyConfig.addPassthroughCopy("slides");

  eleventyConfig.addPassthroughCopy("posts/boundary_cx");
  eleventyConfig.addPassthroughCopy("posts/complex_plotting_plots");

  eleventyConfig.addPlugin(mathjaxPlugin);

  const md = markdownIt({ html: true }).use(markdownItAttrs);
  eleventyConfig.setLibrary("md", md);

  eleventyConfig.addFilter("isoDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).toISODate();
  });

  eleventyConfig.addPairedShortcode("columns", function(content) {
    return `<div class="columns-container">${content}</div>`;
  });

  eleventyConfig.addPairedShortcode("column", function(content) {
    return `<div class="column">${content}</div>`;
  });
}
