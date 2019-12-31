<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto">
                <form v-on:submit.prevent="login">
                    <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
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
                    <button class="btn btn-lg btn-primary btn-block">Sign in</button>
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
      email: '',
      password: '',
      submitted: false,
      loading: false,
      returnUrl: '',
      error: ''
    }
  },
  created () {
    // reset login status
    userService.logout()

    // get return url from route parameters or default to '/'
    this.returnUrl = this.$route.query.returnUrl || '/'
  },

  methods: {
    login () {
      this.submitted = true
      if (!(this.email && this.password)) {
        return
      }
      this.loading = true
      userService.login(this.email, this.password)
        .then(
          user => {
            router.push(this.returnUrl)
            console.log(this.returnUrl)
            console.log(user)
            EventBus.$emit('logged-in', 'loggedin')
          },
          error => {
            this.error = error
            this.loading = false
            EventBus.$emit('')
          }
        )
    },
    emitMethod () {

    }
  }
}

</script>
