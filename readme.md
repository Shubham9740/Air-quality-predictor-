# Air Quality Predictor (PM2.5 Analysis)

A Python-based data analysis tool that analyzes historical PM2.5 air quality data from WHO and predicts future trends for any country using linear regression.

## Features

- **Country-specific analysis** - Analyze PM2.5 data for any country in the WHO dataset
- **Trend calculation** - Automatically calculates whether air quality is improving or worsening
- **Future predictions** - Predicts PM2.5 levels for the next 3 years using gradient-based forecasting
- **Visual representation** - Clean matplotlib graphs showing historical data and predictions
- **Statistical insights** - Displays key metrics including latest values, averages, and yearly change rates

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Libraries
Install the required packages using pip:

```bash
pip install pandas matplotlib numpy scikit-learn
```

Or create a `requirements.txt` file with:
```txt
pandas>=1.3.0
matplotlib>=3.4.0
numpy>=1.21.0
scikit-learn>=0.24.0
```

Then install with:
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Get the Data
Download the WHO PM2.5 air quality dataset and save it as `data.csv` in the same directory as the script.

**Expected CSV structure:**
- ParentLocationCode
- ParentLocation
- SpatialDimValueCode
- Location
- Period type
- Period
- IsLatestYear
- FactValueNumeric

### Step 2: Run the Script
```bash
python air_quality_analysis.py
```

### Step 3: Enter Country Name
When prompted, type the country name you want to analyze:
```
Enter country name: India
```

### Step 4: View Results
The script will display:
- Statistical summary
- 3-year predictions
- A graph with historical data and future predictions

## Example Output

```
==================================================
WHO Air Quality Data Analysis & Prediction
==================================================

Total countries available: 195

Enter country name: India

India - PM2.5 Statistics
--------------------------------------------------
Data available: 2010 - 2019
Number of data points: 10
Latest PM2.5 level: 58.08 μg/m³
Average PM2.5 level: 62.45 μg/m³
Overall trend: Improving (-8.2%)
Gradient: -0.95 μg/m³ per year

Predicted PM2.5 levels for next 3 years:
--------------------------------------------------
Year 2020: 57.13 μg/m³
Year 2021: 56.18 μg/m³
Year 2022: 55.23 μg/m³

Graph displayed successfully!
```

## Understanding the Graph

The graph displays:

- **Blue solid line with dots** - Historical PM2.5 measurements
- **Orange dashed line with dots** - Predicted PM2.5 values for next 3 years
- **Vertical dotted line** - Separates historical data from predictions
- **X-axis** - Years
- **Y-axis** - PM2.5 concentration in μg/m³

## How It Works

### Prediction Algorithm

The tool uses **linear regression** to forecast future PM2.5 levels:

1. **Data Extraction**: Collects all historical PM2.5 measurements for the selected country
2. **Gradient Calculation**: Computes the trend line slope using the least squares method:
   ```
   gradient = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)
   intercept = (Σy - gradient × Σx) / n
   ```
3. **Prediction**: Projects future values by extending the trend line:
   ```
   predicted_PM2.5 = gradient × future_year + intercept
   ```
4. **Validation**: Ensures predictions are non-negative (air quality cannot be negative)

### Why PM2.5?

PM2.5 refers to particulate matter that is 2.5 micrometers or smaller in diameter. These fine particles:
- Can penetrate deep into the lungs and bloodstream
- Are linked to respiratory and cardiovascular diseases
- Are considered the most harmful type of air pollution
- Are a key indicator tracked by WHO for air quality assessment

## Data Source

This project uses WHO (World Health Organization) Ambient Air Quality Database.

Download the dataset from: [WHO Global Health Observatory](https://www.who.int/data/gho)

## Limitations

- **Linear assumption**: Assumes air quality trends follow a linear pattern
- **Short-term accuracy**: Best suited for 2-3 year predictions
- **External factors not considered**: Cannot account for sudden policy changes, natural disasters, or pandemics
- **Data dependency**: Accuracy depends on the quality and consistency of WHO data
- **Country-level analysis**: Does not analyze city-specific or regional variations

## Troubleshooting

### Country Not Found
If you get "No data found for [country name]", the script will show suggestions for similar country names. Common issues:
- Check spelling (e.g., "United States of America" not "USA")
- Try the full official name
- Some territories may be listed separately

### Graph Not Displaying
- Make sure matplotlib is properly installed
- Check if you're running in an environment that supports GUI (not headless server)
- Try running with `plt.show()` in interactive mode

### Missing Data
If a country has insufficient data points (less than 2), predictions cannot be generated. The script will notify you of this limitation.

## Project Structure

```
air-quality-predictor/
├── air_quality_analysis.py    # Main script
├── data.csv                    # WHO PM2.5 data (user provided)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Future Enhancements

Planned improvements include:
- [ ] Multiple prediction models (polynomial, exponential, ARIMA)
- [ ] Confidence intervals for predictions
- [ ] Multi-country comparison mode
- [ ] Export results to CSV/PDF
- [ ] Interactive web interface
- [ ] Regional/city-level analysis
- [ ] Integration with real-time air quality APIs

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- World Health Organization (WHO) for providing comprehensive air quality data
- Python data science community for excellent libraries (pandas, matplotlib, numpy, scikit-learn)
- All contributors and users of this project

## Contact

For questions, suggestions, or bug reports, please open an issue on GitHub.

---

**Note**: Always ensure you have the latest WHO dataset for the most accurate analysis and predictions.

---

## Download Instructions

To use this README:
1. Copy the entire content
2. Save it as `README.md` in your project directory
3. The file will be automatically displayed on GitHub when you push your project

Alternatively, you can download this as a text file and rename it to `README.md`.