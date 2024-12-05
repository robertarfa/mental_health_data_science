# Projeto

### Script

      mkdir data_science_project && cd data_science_project
      poetry init --no-interaction
      poetry add pandas numpy matplotlib seaborn scikit-learn jupyter
      poetry shell
      mkdir -p data/raw data/processed notebooks scripts models
      touch README.md
      touch data/raw/.gitkeep data/processed/.gitkeep
      echo "Estrutura inicial do projeto de Data Science configurada!"

      poetry add streamlit
