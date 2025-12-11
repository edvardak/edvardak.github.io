const markdownIt = require("markdown-it");

module.exports = async function (eleventyConfig) {

  const { katex } = (await import("@mdit/plugin-katex"));

  eleventyConfig.setLibrary(
  	"md,html", 
  	markdownIt().use(katex, {output: "mathml"})
  );

}
