import tkinter as tk
from tkinter import ttk


COLUMNS = ("編號", "姓名", "年齡", "城市")

# 示範資料：包含缺失值及重複資料
RAW_DATA = [
    [1, "小明", 20, "台北"],
    [2, "小華", None, "台中"],
    [3, "小美", 22, None],
    [2, "小華", None, "台中"],
    [4, None, 25, "台北"],
    [3, "小美", 22, None],
    [2, "小華", None, "台中"],
    [4, None, 25, "台北"],
]


def is_missing(value):
    return value is None or (isinstance(value, str) and value.strip() == "")


def fill_missing(data):
    """使用欄位最常出現的值補缺失；整欄皆缺失時填入「未知」。"""
    result = [row.copy() for row in data]

    for column_index in range(len(COLUMNS)):
        values = [
            row[column_index]
            for row in data
            if not is_missing(row[column_index])
        ]
        fill_value = max(values, key=values.count) if values else "未知"

        for row in result:
            if is_missing(row[column_index]):
                row[column_index] = fill_value

    return result


def remove_duplicates(data):
    """刪除完全相同的資料列，保留第一次出現的資料。"""
    result = []
    seen = set()

    for row in data:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            result.append(row.copy())

    return result


class DataViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("原始資料與資料清理")
        self.root.geometry("900x700")
        self.result_tabs = {}

        self._create_original_view()
        self._create_buttons()
        self._create_result_view()
        self._show_data(self.original_tree, RAW_DATA)

    def _create_treeview(self, parent, height=6):
        tree = ttk.Treeview(parent, columns=COLUMNS, show="headings", height=height)

        for column in COLUMNS:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        y_scrollbar = ttk.Scrollbar(
            parent, orient="vertical", command=tree.yview
        )
        x_scrollbar = ttk.Scrollbar(
            parent, orient="horizontal", command=tree.xview
        )
        tree.configure(
            yscrollcommand=y_scrollbar.set,
            xscrollcommand=x_scrollbar.set,
        )

        tree.grid(row=0, column=0, sticky="nsew")
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        x_scrollbar.grid(row=1, column=0, sticky="ew")

        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        return tree

    def _create_original_view(self):
        frame = ttk.LabelFrame(self.root, text="原始資料")
        frame.pack(fill="both", expand=True, padx=10, pady=(10, 5))
        self.original_tree = self._create_treeview(frame, height=1)

    def _create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(
            button_frame,
            text="刪除重複",
            command=self.show_deduplicated,
        ).pack(side="left", expand=True, fill="x", padx=5)

        ttk.Button(
            button_frame,
            text="補上缺失值",
            command=self.show_filled,
        ).pack(side="left", expand=True, fill="x", padx=5)

        ttk.Button(
            button_frame,
            text="補上缺失＋刪除重複值",
            command=self.show_filled_and_deduplicated,
        ).pack(side="left", expand=True, fill="x", padx=5)

    def _create_result_view(self):
        frame = ttk.LabelFrame(self.root, text="處理結果")
        frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        self.notebook = ttk.Notebook(frame)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

    def _show_data(self, tree, data):
        tree.delete(*tree.get_children())

        for row in data:
            display_row = [
                "（缺失）" if is_missing(value) else value
                for value in row
            ]
            tree.insert("", "end", values=display_row)

    def _show_result(self, tab_name, title, data):
        if tab_name not in self.result_tabs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=title)
            tree = self._create_treeview(tab, height=6)
            self.result_tabs[tab_name] = (tab, tree)
        else:
            tab, tree = self.result_tabs[tab_name]
            self.notebook.tab(tab, text=title)

        self._show_data(tree, data)
        self.notebook.select(self.result_tabs[tab_name][0])

    def show_deduplicated(self):
        self._show_result(
            "deduplicate",
            "刪除重複",
            remove_duplicates(RAW_DATA),
        )

    def show_filled(self):
        self._show_result(
            "fill",
            "補上缺失值",
            fill_missing(RAW_DATA),
        )

    def show_filled_and_deduplicated(self):
        result = remove_duplicates(fill_missing(RAW_DATA))
        self._show_result(
            "fill_deduplicate",
            "補缺失＋刪重複",
            result,
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = DataViewer(root)
    root.mainloop()
