from langchain_community.llms import Ollama

ollama_openhermes = Ollama(model="openhermes")
ollama_mistral = Ollama(model="mistral")
ollama_llama = Ollama(model="llama2")
currentModel = ollama_llama

class OllamaModelManager():


    def getDefaultModel():
        return currentModel
    
    def getLlamaModel():
        return ollama_llama
    
    def getMistralModel():
        return ollama_mistral
    
    def getOpenHermesModel():
        return ollama_openhermes