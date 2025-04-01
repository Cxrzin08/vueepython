<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const usuarios = ref([])
const isLoading = ref(true)
const error = ref(null)

const fetchUsuarios = async () => {
  try {
    const response = await axios.get('http://localhost:5000/pegar-usuarios')
    usuarios.value = response.data.usuarios
  } catch (err) {
    error.value = 'Erro ao carregar usuários. Tente recarregar a página.'
    console.error('Erro:', err)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchUsuarios()
})
</script>

<template>
  <div class="container">
    <h2>Lista de Usuários</h2>
    
    <div v-if="isLoading" class="loading">
      Carregando usuários...
    </div>
    
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    
    <div v-else-if="usuarios.length === 0" class="empty">
      Nenhum usuário cadastrado ainda.
    </div>
    
    <ul v-else class="user-list">
      <li v-for="(usuario, index) in usuarios" :key="index" class="user-item">
        {{ usuario }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
}

.loading, .error, .empty {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.error {
  color: #ff4444;
}

.user-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.user-item {
  padding: 1rem;
  margin-bottom: 0.5rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.user-item:hover {
  background-color: #e9ecef;
}
</style>