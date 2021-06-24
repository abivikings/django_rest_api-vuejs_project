<template>
  <nav class="navbar navbar-expand-sm bg-info navbar-dark">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <router-link to="/" class="nav-link">Vue Frontend</router-link>
      </li>

      <li class="nav-item">
        <router-link to="/registration" class="nav-link">Add User</router-link>
      </li>

      <li class="nav-item">
        <router-link to="/add_item" class="nav-link">Add Item</router-link>
      </li>

      <li class="nav-item">
        <router-link to="/registration" class="nav-link"
          >Store View</router-link
        >
      </li>

      <li class="nav-item">
        <router-link to="/logout" class="nav-link">Logout</router-link>
      </li>
    </ul>
  </nav>
</template>