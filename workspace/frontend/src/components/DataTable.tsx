import type { ReactNode } from "react";

interface DataTableProps<T> {
  rows: T[];
  columns: Array<{ label: string; render: (row: T) => ReactNode }>;
}

export function DataTable<T>({ rows, columns }: DataTableProps<T>) {
  return (
    <div className="tableWrap">
      <table>
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={column.label}>{column.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              {columns.map((column) => (
                <td key={column.label}>{column.render(row)}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
