import React from "react";
import DarkModeToggle from "./components/DarkModeToggle";

function App() {
  return (
    <div className="min-h-screen bg-white text-black dark:bg-gray-900 dark:text-gray-100">
      <header className="p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold">Sierra Leone IELTS Prep</h1>
        <DarkModeToggle />
      </header>

      <main className="p-6">
        <p>Welcome to the IELTS preparation platform.</p>
      </main>
    </div>
  );
}

export default App;
