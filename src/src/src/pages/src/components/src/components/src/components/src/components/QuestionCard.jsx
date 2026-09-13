export default function QuestionCard({ question, options, onAnswer }) {
  return (
    <div className="border p-4 rounded shadow-md">
      <h2 className="font-semibold">{question}</h2>
      <ul className="mt-2 space-y-2">
        {options.map((opt, idx) => (
          <li key={idx}>
            <button
              className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-700"
              onClick={() => onAnswer(opt)}
            >
              {opt}
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
