<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const message = ref('')
const isLoading = ref(false)
const router = useRouter()

const cadastrarUsuario = async () => {
  if (!username.value.trim()) {
    message.value = 'Por favor, insira um nome de usuário'
    return
  }

  isLoading.value = true
  message.value = ''

  try {
    const response = await axios.post('http://localhost:5000/novo-usuario', {
      nome: username.value.trim()
    })
    
    message.value = response.data.message
    username.value = ''
    
    setTimeout(() => router.push('/usuarios'), 1500)
    
  } catch (error) {
    if (error.response) {
      message.value = error.response.data.message || 'Erro ao cadastrar'
    } else {
      message.value = 'Servidor não disponível. Tente novamente.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="container">
    <h2>Cadastrar Novo Usuário</h2>
    <div class="form-group">
      <input
        v-model="username"
        placeholder="Digite o nome do usuário"
        type="text"
        class="form-input"
        @keyup.enter="cadastrarUsuario"
      >
    </div>
    <button 
      @click="cadastrarUsuario"
      :disabled="isLoading"
      class="submit-btn"
    >
      {{ isLoading ? 'Cadastrando...' : 'Cadastrar' }}
    </button>
    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<style scoped>
.container {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.submit-btn {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #369f6b;
}

.submit-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.message {
  margin-top: 1rem;
  color: #42b983;
  font-size: 0.9rem;
}
</style>