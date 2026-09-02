const form = document.querySelector("#salary-form");
const currentSalaryInput = document.querySelector("#current-salary");
const newSalaryInput = document.querySelector("#new-salary");
const calculateButton = document.querySelector(".calculate-btn");
const resetButton = document.querySelector(".reset-btn");
const currentError = document.querySelector("#current-error");
const newError = document.querySelector("#new-error");
const statusPill = document.querySelector("#status-pill");
const percentValue = document.querySelector("#percent-value");
const percentDisplay = document.querySelector("#percent-display");
const currentDisplay = document.querySelector("#current-display");
const newDisplay = document.querySelector("#new-display");
const amountDisplay = document.querySelector("#amount-display");
const insightText = document.querySelector("#insight-text");
const percentageRing = document.querySelector("#percentage-ring");
const compareCurrent = document.querySelector("#compare-current");
const compareNew = document.querySelector("#compare-new");
const currentBar = document.querySelector("#current-bar-fill");
const newBar = document.querySelector("#new-bar-fill");
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector("#nav-links");
const themeToggle = document.querySelector(".theme-toggle");
const exampleTrigger = document.querySelector("#example-trigger");
const exampleCards = document.querySelectorAll(".example-card");
const copyResultBtn = document.querySelector("#copy-result");
const printResultBtn = document.querySelector("#print-result");
const periodButtons = document.querySelectorAll(".segment");

let selectedPeriod = "yearly";

function formatCurrency(value) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

function formatSalary(value, period = selectedPeriod) {
  const adjustedValue = period === "monthly" ? value / 12 : value;
  const suffix = period === "monthly" ? "/ month" : "LPA";
  return `${formatCurrency(adjustedValue)} ${suffix}`;
}

function setStatus(state) {
  statusPill.className = "status-pill";
  if (state === "positive") {
    statusPill.textContent = "High growth";
    statusPill.classList.add("positive");
  } else if (state === "negative") {
    statusPill.textContent = "Lower";
    statusPill.classList.add("negative");
  } else if (state === "neutral") {
    statusPill.textContent = "Stable";
    statusPill.classList.add("neutral");
  } else {
    statusPill.textContent = "Ready";
    statusPill.classList.add("neutral");
  }
}

function updateRing(value) {
  const boundedValue = Math.min(Math.abs(value), 100);
  const angle = (boundedValue / 100) * 360;
  percentageRing.style.setProperty("--ring-value", `${angle}deg`);

  const ringColor = value >= 0 ? "var(--primary)" : "var(--danger)";
  percentageRing.style.background = `conic-gradient(${ringColor} ${angle}deg, rgba(161, 178, 209, 0.24) 0deg)`;
}

function clearErrors() {
  currentError.textContent = "";
  newError.textContent = "";
}

function resetResults() {
  currentDisplay.textContent = "₹0.00 LPA";
  newDisplay.textContent = "₹0.00 LPA";
  amountDisplay.textContent = "₹0.00 LPA";
  percentDisplay.textContent = "0.00%";
  percentValue.textContent = "0.00%";
  setStatus("neutral");
  insightText.textContent = "Enter your current and new salaries to estimate your salary growth.";
  percentageRing.style.background = "conic-gradient(var(--primary) 0deg, rgba(161, 178, 209, 0.24) 0deg)";
  compareCurrent.textContent = "₹5.00 LPA";
  compareNew.textContent = "₹7.50 LPA";
  currentBar.style.width = "50%";
  newBar.style.width = "70%";
}

function validateInput(currentValue, newValue) {
  clearErrors();

  if (!currentSalaryInput.value.trim() || Number(currentValue) <= 0) {
    currentError.textContent = "Current salary must be greater than zero.";
    currentSalaryInput.focus();
    return false;
  }

  if (!newSalaryInput.value.trim() || Number(newValue) < 0) {
    newError.textContent = "New salary cannot be negative.";
    newSalaryInput.focus();
    return false;
  }

  if (Number(newValue) <= 0) {
    newError.textContent = "New salary should be greater than zero for a valid hike.";
    newSalaryInput.focus();
    return false;
  }

  if (!Number.isFinite(currentValue) || !Number.isFinite(newValue)) {
    if (!Number.isFinite(currentValue)) {
      currentError.textContent = "Please enter a valid number for the current salary.";
    }
    if (!Number.isFinite(newValue)) {
      newError.textContent = "Please enter a valid number for the new salary.";
    }
    return false;
  }

  return true;
}

function setPeriod(period) {
  selectedPeriod = period;
  periodButtons.forEach((button) => {
    const isActive = button.dataset.period === period;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-pressed", String(isActive));
  });
}

function applyExample(current, next) {
  currentSalaryInput.value = current;
  newSalaryInput.value = next;
  setPeriod("yearly");
  calculateSalary();
}

function calculateSalary() {
  const currentValue = Number(currentSalaryInput.value);
  const newValue = Number(newSalaryInput.value);

  if (!validateInput(currentValue, newValue)) {
    return;
  }

  const hikeAmount = newValue - currentValue;
  const hikePercentage = (hikeAmount / currentValue) * 100;

  currentDisplay.textContent = formatSalary(currentValue);
  newDisplay.textContent = formatSalary(newValue);
  amountDisplay.textContent = formatSalary(hikeAmount);

  const percentText = `${Math.abs(hikePercentage).toFixed(2)}%`;
  percentDisplay.textContent = `${hikePercentage >= 0 ? "+" : "-"}${percentText}`;
  percentValue.textContent = `${Math.abs(hikePercentage).toFixed(2)}%`;
  updateRing(hikePercentage);

  const compareMax = Math.max(currentValue, newValue) || 1;
  currentBar.style.width = `${(currentValue / compareMax) * 100}%`;
  newBar.style.width = `${(newValue / compareMax) * 100}%`;

  compareCurrent.textContent = formatSalary(currentValue);
  compareNew.textContent = formatSalary(newValue);

  if (hikePercentage > 0) {
    setStatus("positive");
    insightText.textContent = `Your salary increased by ${formatSalary(hikeAmount)}.`;
  } else if (hikePercentage < 0) {
    setStatus("negative");
    insightText.textContent = `Your salary decreased by ${formatSalary(Math.abs(hikeAmount))}.`;
  } else {
    setStatus("neutral");
    insightText.textContent = "Your salary has not changed.";
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  calculateButton.classList.add("loading");
  calculateButton.disabled = true;

  window.setTimeout(() => {
    calculateSalary();
    calculateButton.classList.remove("loading");
    calculateButton.disabled = false;
  }, 500);
});

resetButton.addEventListener("click", () => {
  form.reset();
  clearErrors();
  setPeriod("yearly");
  resetResults();
  currentSalaryInput.focus();
});

[currentSalaryInput, newSalaryInput].forEach((input) => {
  input.addEventListener("input", () => {
    clearErrors();
    if (!input.value.trim()) {
      resetResults();
    }
  });
});

periodButtons.forEach((button) => {
  button.addEventListener("click", () => {
    setPeriod(button.dataset.period);
    if (currentSalaryInput.value || newSalaryInput.value) {
      calculateSalary();
    }
  });
});

navToggle.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const themeIcon = themeToggle.querySelector(".theme-icon");
  themeIcon.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});

exampleTrigger.addEventListener("click", () => {
  applyExample(5, 6);
});

exampleCards.forEach((card) => {
  card.addEventListener("click", () => {
    const current = Number(card.dataset.current);
    const next = Number(card.dataset.new);
    applyExample(current, next);
  });
});

copyResultBtn.addEventListener("click", async () => {
  const resultText = `Current Salary: ${currentDisplay.textContent}\nNew Salary: ${newDisplay.textContent}\nHike Amount: ${amountDisplay.textContent}\nHike Percentage: ${percentDisplay.textContent}`;

  try {
    await navigator.clipboard.writeText(resultText);
    copyResultBtn.textContent = "Copied";
    window.setTimeout(() => {
      copyResultBtn.textContent = "Copy result";
    }, 1200);
  } catch (error) {
    copyResultBtn.textContent = "Copy failed";
    window.setTimeout(() => {
      copyResultBtn.textContent = "Copy result";
    }, 1200);
  }
});

printResultBtn.addEventListener("click", () => {
  window.print();
});

resetResults();
