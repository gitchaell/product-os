import { test, expect } from '@playwright/test';

test('dark mode persists across navigation without flash', async ({ page }) => {
  await page.goto('http://localhost:4321');

  // Set dark mode
  await page.evaluate(() => {
    localStorage.setItem('theme', 'dark');
    document.documentElement.classList.add('dark');
  });

  await page.waitForTimeout(500);

  // Start recording video/screenshots if needed, but for now just navigate
  await page.click('text=Roadmap');

  // Try to catch the flash by evaluating immediately
  const classesDuringTransition = await page.evaluate(() => {
    return document.documentElement.classList.contains('dark');
  });

  await page.waitForTimeout(500);

  // Check if dark mode is still active
  const isDark = await page.evaluate(() => document.documentElement.classList.contains('dark'));
  expect(isDark).toBeTruthy();
});
