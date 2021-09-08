/* global Then, When */
/* eslint no-console: ["error", { allow: ["warn","log"] }] */
let code = "";
let argString = "";
// eslint-disable-next-line prefer-const
let variableToVerify = ""; // we are assigning this through eval

console.log(window);

When("I use DocString for code like this:", (dataString) => {
  code = dataString;
});

When("I use DocString with argument like this:", (dataString) => {
  argString = dataString;
});

Then("I ran it and verify that it executes it", () => {
  // eslint-disable-next-line no-eval
  eval(code);
  expect(variableToVerify).to.equal("hello world");
});

let freemarkerSnippet = "";
When("I use DocString for freemarker code like this", (dataString) => {
  freemarkerSnippet = dataString;
});

Then("I can interpret it as a string", () => {
  expect(freemarkerSnippet).to.be.a("string");
});

Then(/^I should have a string with argument "([^"]*)"$/, (argument) => {
  expect(argString).to.contain(argument);
});
