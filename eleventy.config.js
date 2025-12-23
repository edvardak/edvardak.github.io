const mathjaxPlugin = require("eleventy-plugin-mathjax");
const { DateTime } = require("luxon");


module.exports = async function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("style.css");
  eleventyConfig.addPassthroughCopy("slides");

  eleventyConfig.addPlugin(mathjaxPlugin);

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
