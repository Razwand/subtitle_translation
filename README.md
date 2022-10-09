# 🎬 Subtitle Translation 🎬 

This repo contains a tool to translate .str subtitles file from English to Spanish:
    
![Sample](https://github.com/Razwand/subtitle_translation/blob/master/images/samples.PNG)

## Requirements
- A suitable conda environment named translate_subs can be created and activated with:

```console
conda env create -f environment_subs.yml
```
```console
conda activate translate_subs
```

## Context

The idea is to convert a file containing English subtitles with the structure of a str file into the Spanish version of it. A translation model is used to get the predictions (text in Spanish).

### About the structure of a .str file
Subtitle files considered for this tool are .srt files. The structure of these files is the following:

![STRFILE](https://github.com/Razwand/subtitle_translation/blob/master/images/structure_file_srt.PNG)

### About the model

The model used for translation has been trained and host at HugginFace hub:

🤗[Translation Model](https://huggingface.co/razwand/opus-mt-en-mul-finetuned_en_sp_translator)

## How to
⚠️Note:  original .srt **must** be saved as a .txt file.

The following scenario shows how to translate an original file with English subtitles into Spanish.

```console
subtitle_translation>python translate_my_subs.py HTWJW_1.txt

```



