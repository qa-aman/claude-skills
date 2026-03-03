---
name: write-tests
description: >
  Write unit and integration tests. Use when the user says "write tests for this",
  "add test coverage", "how do I test this", "TDD", "red green refactor",
  "unit test this function", "test this module", "I need tests for", or has code
  that lacks tests - even if they don't explicitly say "write tests".
---

## Overview

Based on **"Test Driven Development By Example"** by Kent Beck. Beck's core insight: tests are not a tax on development - they are the way you design. Writing the test first forces you to think about the interface before the implementation. Code written test-first tends to be more modular, more focused, and easier to change.

The TDD cycle: **Red - Green - Refactor**
- **Red:** Write a failing test that defines desired behavior
- **Green:** Write the minimum code to make the test pass
- **Refactor:** Clean up the code without changing behavior. Tests prove you haven't broken anything.

## Workflow

### Step 1: Identify what to test
For a given function or module, list the behaviors to test:
- The happy path (valid inputs - correct output)
- Invalid inputs (what should fail gracefully)
- Boundary conditions (empty, null, max, min)
- Edge cases (concurrent calls, large data, unexpected types)

Don't write tests for implementation details - test behavior.

### Step 2: Write the failing test first (Red)
Write a test that:
- Has a descriptive name: `test_<action>_<condition>_<expected_result>`
- Tests one behavior per test
- Has clear Arrange / Act / Assert structure

Example in Python:
```python
def test_withdraw_fails_when_balance_insufficient():
    # Arrange
    account = BankAccount(balance=50)
    # Act + Assert
    with pytest.raises(InsufficientFundsError):
        account.withdraw(100)
```

Run the test. Confirm it fails for the right reason (not a syntax error).

### Step 3: Write minimum code to pass (Green)
Write the simplest code that makes the test pass.
Do not gold-plate. Do not add features not tested yet.
Run the test. Confirm it passes.

### Step 4: Refactor (Refactor)
Clean up:
- Remove duplication
- Improve naming
- Extract functions if needed

Run all tests after each refactor step. Tests are the safety net.

### Step 5: Repeat for each behavior
Add one test at a time. After each Red-Green-Refactor cycle, all tests should pass.

### Step 6: Write integration tests for wiring
Unit tests cover individual functions. Integration tests cover how components connect.
- Test the integration point (API call, DB write, external service)
- Use test doubles (mocks, stubs, fakes) for external dependencies in unit tests
- Use real dependencies in integration tests

## Anti-Patterns

**1. Testing implementation instead of behavior**
Bad: Testing that a specific private method was called.
Good: Testing that the observable output is correct given the input.

**2. Tests that depend on each other**
Bad: Test B only works if Test A ran first.
Good: Each test is fully independent. Any test can run in any order.

**3. Writing tests after the code**
Bad: Code written first, tests added later to hit coverage targets.
Good: Test first. The discipline is the point - it changes how you design.

**4. One massive test instead of many small ones**
Bad: One test that covers 10 behaviors.
Good: One behavior per test. When a test fails, you know exactly what broke.

## Quality Checklist

- [ ] Test names describe behavior: `test_action_condition_result`
- [ ] Each test covers exactly one behavior
- [ ] Tests follow Arrange / Act / Assert structure
- [ ] Tests run in any order (no interdependencies)
- [ ] Happy path, invalid inputs, and boundary conditions covered
- [ ] External dependencies mocked in unit tests
- [ ] Failing test written and confirmed failing before implementation
- [ ] All tests pass after implementation and refactor
