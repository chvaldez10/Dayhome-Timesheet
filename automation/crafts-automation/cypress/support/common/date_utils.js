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

function padNumber(num) {
  return num < 10 ? "0" + num : num;
}

Cypress.Commands.add("traverseDate", (month, year, monthName) => {
  const expectedDays = getExpectedDaysInMonth(month, year);
  const monthPadded = padNumber(month);
  const timeoutTime = 5000;
  const waitTime = 3000;

  cy.log(`Traversing date for month: ${month} and year: ${year}`);
  cy.clickDateInput(monthName);

  // GIVEN expected days array
  // WHEN we traverse the array and click on each day
  // THEN all days in the array should all exist
  expectedDays.forEach((day, numDays) => {
    numDays += 1;
    const dayPadded = padNumber(numDays);
    const outputFilename = `cypress/downloads/${year}-${monthPadded}-${dayPadded}.csv`;

    cy.clickDateInput(monthName);
    cy.get(`[aria-label='${day}']`).should("exist").click();
    cy.wait(timeoutTime);
    cy.get("a.buttons-csv span").contains("CSV").click();

    cy.readFile(Cypress.env("expectedCraftsCsv"), "binary", {
      timeout: timeoutTime,
    }).then((fileContent) => {
      cy.writeFile(outputFilename, fileContent, "binary");
    });

    cy.wait(waitTime);
  });
});
