export default function Card({ title, value, color, details }) {
  const colorMap = {
    green: "bg-green-600",
    red: "bg-red-600",
    yellow: "bg-yellow-500",
    gray: "bg-gray-600",
  };

  return (
    <div className="p-5 rounded-lg shadow-md bg-gray-800 text-white flex flex-col gap-3 w-full h-auto break-words">
      
      {/* Title */}
      <span className="text-base font-semibold break-words whitespace-normal">
        {title}
      </span>

      {/* Value */}
      <div className="text-lg font-medium break-all whitespace-normal">
        {value}
      </div>

      {/* Status dot */}
      <div className={`h-3 w-3 rounded-full ${colorMap[color] || "bg-gray-600"}`} />

      {/* Optional expandable details */}
      {details && (
        <details className="mt-2 bg-gray-900 p-2 rounded">
          <summary className="cursor-pointer text-sm font-semibold">
            Details
          </summary>
          <pre className="mt-2 text-xs whitespace-pre-wrap">
            {details}
          </pre>
        </details>
      )}
    </div>
  );
}
