Cypress.Commands.add("clickDateInput", (monthName) => {
  cy.get("input[placeholder='Pick date']").click();
  cy.get(".flatpickr-current-month .cur-month").should("contain", monthName);
});
