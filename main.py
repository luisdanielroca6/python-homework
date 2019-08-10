{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pathlib import Path\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('budget_data.csv', delimiter = ',')\n",
    "\n",
    "\n",
    "\n",
    "cashflows = df[['Profit/Losses']]\n",
    "\n",
    "total = cashflows.sum()\n",
    "\n",
    "months = len(cashflows)\n",
    "\n",
    "drop = df.drop(0)\n",
    "drop[\"Period_Returns\"] = drop['Profit/Losses'].cumsum(0)\n",
    "period_return = drop[\"Period_Returns\"].mean()\n",
    "\n",
    "period_return\n",
    "\n",
    "max_index = df['Profit/Losses'].idxmax():]\n",
    "\n",
    "\n",
    "max_amt = df.iloc[max_index,:]\n",
    "\n",
    "\n",
    "min_index = df['Profit/Losses'].idxmin()\n",
    "\n",
    "\n",
    "min_amt = df.iloc[min_index,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('output.txt', 'w') as d:\n",
    "    mydict = dict({\n",
    "'Total Months': months,\n",
    "'Total': total,\n",
    "'Average  Change': period_return,\n",
    "'Greatest Increase in Profits': max_amt,\n",
    "'Greatest Decrease in Profits': min_amt})\n",
    "    d.write(str(mydict))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
