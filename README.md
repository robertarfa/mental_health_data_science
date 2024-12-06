# Project Hypertension prevalence Analysis

https://data.who.int/indicators/i/7DA4E68/608DE39

### Script

      mkdir data_science_project && cd data_science_project
      poetry init --no-interaction
      poetry add pandas numpy matplotlib seaborn jupyter tabula-py openpyxl scikit-learn
      poetry shell
      mkdir -p data/raw data/processed notebooks scripts models
      touch README.md
      touch data/raw/.gitkeep data/processed/.gitkeep
      echo "Estrutura inicial do projeto de Data Science configurada!"

      poetry add streamlit

      1 - Install
      sudo apt install xdg-utils
      2 -  Download
      wget https://iris.who.int/bitstream/handle/10665/345946/9789240036703-eng.pdf
      3 - New File
      touch scripts/extract_who_data.py
