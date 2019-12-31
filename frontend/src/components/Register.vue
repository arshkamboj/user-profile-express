<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto">
                <form v-on:submit.prevent="register">
                    <h1 class="h3 mb-3 font-weight-normal">Register</h1>
                    <div class="form-group">
                        <label for="firstName">First Name</label>
                        <input type="text" v-model="firstName" class="form-control" name="firstName" placeholder="Enter First Name" :class="{ 'is-invalid': submitted && !firstName }" />
                        <div v-show="submitted && !firstName" class="invalid-feedback">First Name is required</div>
                    </div>
                    <div class="form-group">
                        <label for="lastName">Last Name</label>
                        <input type="text" v-model="lastName" class="form-control" name="lastName" placeholder="Enter Last Name" :class="{ 'is-invalid': submitted && !lastName }" />
                        <div v-show="submitted && !lastName" class="invalid-feedback">Last Name is required</div>
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" v-model="email" class="form-control" name="email" placeholder="Enter Email" :class="{ 'is-invalid': submitted && !email }" />
                        <div v-show="submitted && !email" class="invalid-feedback">Email Id is required</div>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" v-model="password" class="form-control" name="password" placeholder="Enter Password" :class="{ 'is-invalid': submitted && !password }" />
                        <div v-show="submitted && !password" class="invalid-feedback">Password is required</div>
                    </div>
                    <button class="btn btn-lg btn-primary btn-block">Register</button>
                    <div v-if="error" class="alert alert-danger">{{error}}</div>
                </form>
            </div>
        </div>
    </div>

</template>

<script>
import router from '../router'
import EventBus from './EventBus'
import { userService } from './_services'

export default {
  data () {
    return {
      firstName: '',
      lastName: '',
      email: '',
      submitted: false,
      loading: false,
      password: '',
      returnUrl: '/login',
      error: ''
    }
  },

  methods: {
    register () {
      this.submitted = true
      if (!(this.firstName && this.lastName && this.email && this.password)) {
        return
      }
      userService.register(this.firstName, this.lastName, this.email, this.password)
        .then(
          user => {
            router.push(this.returnUrl)
          },
          error => {
            this.error = error
            this.loading = false
            EventBus.$emit('')
          }
        )
    }
  }
}

</script>
