/* global Given, Then */
/* eslint no-console: ["error", { allow: ["log"] }] */
let counter = 0;
console.log(window);
Given("counter is incremented", () => {
  counter += 1;
});

Then("counter equals {int}", (value) => {
  expect(counter).to.equal(value);
});
