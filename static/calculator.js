document.addEventListener("DOMContentLoaded", function () {
  // Get all the elements
  const loanAmountInput = document.getElementById("loan-amount");
  const loanTermInput = document.getElementById("loan-term");
  const loanAmountDisplay = document.getElementById("loan-amount-display");
  const loanTermDisplay = document.getElementById("loan-term-display");

  const monthlyPaymentDisplay = document.getElementById("monthly-payment");
  const totalPaymentDisplay = document.getElementById("total-payment");
  const totalInterestDisplay = document.getElementById("total-interest");

  // Set fixed interest rate (like Capfin)
  const interestRate = 30; // 30% annual rate (adjust to your company's rate)

  // Function to format currency
  function formatCurrency(value) {
    return (
      "R" +
      parseFloat(value)
        .toFixed(2)
        .replace(/\d(?=(\d{3})+\.)/g, "$&,")
    );
  }

  // Function to calculate loan payments
  function calculateLoan() {
    // Get current values
    const principal = parseFloat(loanAmountInput.value);
    const monthlyRate = interestRate / 100 / 12;
    const months = parseInt(loanTermInput.value);

    // Calculate monthly payment
    let monthlyPayment = 0;
    if (monthlyRate !== 0) {
      monthlyPayment =
        (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));
    } else {
      monthlyPayment = principal / months;
    }

    // Calculate total payment and interest
    const totalPayment = monthlyPayment * months;
    const totalInterest = totalPayment - principal;

    // Update displays
    loanAmountDisplay.textContent = formatCurrency(principal);
    loanTermDisplay.textContent = months + " months";

    if (isFinite(monthlyPayment) && monthlyPayment > 0) {
      monthlyPaymentDisplay.textContent = formatCurrency(monthlyPayment);
      totalPaymentDisplay.textContent = formatCurrency(totalPayment);
      totalInterestDisplay.textContent = formatCurrency(totalInterest);
    } else {
      monthlyPaymentDisplay.textContent = "R0.00";
      totalPaymentDisplay.textContent = "R0.00";
      totalInterestDisplay.textContent = "R0.00";
    }
  }

  // Set up event listeners
  if (loanAmountInput && loanTermInput) {
    loanAmountInput.addEventListener("input", calculateLoan);
    loanTermInput.addEventListener("input", calculateLoan);

    // Initialize with default values
    calculateLoan();
  }
});
