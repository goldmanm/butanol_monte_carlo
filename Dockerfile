#This is a sample Image 
FROM continuumio/miniconda3

RUN git clone https://www.github.com/goldmanm/butanol_monte_carlo.git /home/repo_monte_carlo

RUN conda env create -f /home/repo_monte_carlo/environment.yml
RUN echo "source activate $(head -1 /home/repo_monte_carlo/environment.yml | cut -d' ' -f2)" > ~/.bashrc

