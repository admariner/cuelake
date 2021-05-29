import React from "react";
import NotebookTable from "components/Notebooks/NotebookTable.js";


export default function NotebookTableFunction() {
  return (
    <>
      <div className="flex flex-wrap mh-full">
        <div className="w-full mb-12 px-4">
		      <NotebookTable />
        </div>
      </div>
    </>
  );
}
