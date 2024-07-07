function getExpectedDaysInMonth(month, year) {
  var date = new Date(year, month - 1, 1);
  var days = [];
  var options = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };

  while (date.getMonth() === month - 1) {
    days.push(date.toLocaleDateString("en-US", options));
    date.setDate(date.getDate() + 1);
  }
  return days;
}

Cypress.Commands.add("traverseDate", (month, year, monthName) => {
  const expectedDays = getExpectedDaysInMonth(month, year);

  cy.log(`Traversing date for month: ${month} and year: ${year}`);

  // GIVEN expected days array
  // WHEN we traverse the array and click on each day
  // THEN all days in the array should all exist
  expectedDays.forEach((day, index) => {
    cy.clickDateInput(monthName);
    cy.get("[aria-label='" + day + "']")
      .should("exist")
      .click();
  });
});
