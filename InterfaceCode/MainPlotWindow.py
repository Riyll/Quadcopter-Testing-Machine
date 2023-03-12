import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QInputDialog, QSpinBox, QTabWidget, QHBoxLayout, QLineEdit
import pandas as pd
import matplotlib.pyplot as plt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label to display the file path
        self.file_label = QLabel('No file selected', self)

        # Create a button to open a file dialog and load the Excel file
        self.button = QPushButton('Select file', self)
        self.button.clicked.connect(self.loadFile)

        # Create a combo box to select the x-axis column
        self.xaxis_label = QLabel('Select x-axis column:', self)
        self.xaxis_combobox = QComboBox(self)
        self.xaxis_combobox.setEnabled(False)
        self.xaxis_combobox.currentIndexChanged.connect(self.plotGraphs)

        # Create spin boxes to input the Px, Py, Pz, Tx, Ty, and Tz values
        
        # Create a layout for the tab with variable inputs
        variables_tab_layout = QVBoxLayout()
        

        # Create a new tab widget and add the variables tab
        self.tab_widget = QTabWidget(self)
        
        variables_tab = QWidget()
        variables_tab.setLayout(variables_tab_layout)
        self.tab_widget.addTab(variables_tab, 'Graphs')

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.button)
        layout.addWidget(self.xaxis_label)
        layout.addWidget(self.xaxis_combobox)
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

        # Set window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('PyQt5 Graph Example')
        self.show()

    def loadFile(self):
        
        
        

         # Load the Excel file into a pandas dataframe
        df = pd.read_excel("dummyvalues.xlsx")

        # Enable the x-axis combo box and populate it with the column names
        self.xaxis_combobox.setEnabled(True)
        self.xaxis_combobox.addItems(df.columns)


    def plotGraphs(self):
        # Get the selected x-axis column
        xaxis_column = self.xaxis_combobox.currentText()

        # Load the Excel file into a pandas dataframe
        df = pd.read_excel("dummyvalues.xlsx")

        # Create a list of columns that have data
        columns_with_data = [column for column in df.columns if df[column].notnull().any()]

        # Create the subplots and plot the data
        num_plots = len(columns_with_data)   # Subtract 1 to generate 11 plots
        num_rows = 3
        num_cols = 4
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 8))
        for i, column in enumerate(columns_with_data):
            if column != xaxis_column and i < num_plots:  # Check if i < num_plots to generate 11 plots
                row = (i - 1) // num_cols  # Subtract 1 to skip the x-axis column
                col = (i - 1) % num_cols
                axs[row, col].plot(df[xaxis_column][df[column].notnull()], df[column][df[column].notnull()])
                axs[row, col].set_title(column)

        # Set the x-axis label and display the plot
        fig.text(0.5, 0.04, xaxis_column, ha='center')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
