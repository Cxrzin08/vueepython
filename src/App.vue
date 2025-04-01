<template>
  <div id="app">
    <header>
      <h1>Gerenciador de Usuários</h1>
      <nav>
        <router-link to="/">Cadastrar</router-link> |
        <router-link to="/usuarios">Listar</router-link>
      </nav>
    </header>
    
    <main>
      <router-view />
    </main>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

header {
  text-align: center;
  padding: 1rem;
  background-color: #f8f9fa;
  margin-bottom: 2rem;
}

nav {
  padding: 1rem;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #e9ecef;
}

nav a.router-link-exact-active {
  color: #42b983;
}

main {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem;
}
</style>