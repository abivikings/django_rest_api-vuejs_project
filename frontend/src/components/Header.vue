<template>
  <nav class="navbar navbar-expand-sm bg-info navbar-dark">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Vue Frontend</a>
      </li>

      <li class="nav-item">
        <router-link to="/login" class="nav-link">Login</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/registration" class="nav-link"
          >Registration</router-link
        >
      </li>
    </ul>
  </nav>
</template>