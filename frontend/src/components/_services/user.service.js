import { authHeader } from '../_helpers/auth-header'
export const userService = {
  login,
  logout,
  register,
  getProfileInformation,
  uploadUserProfileImage,
  updateProfile,
  getAll
}

function login (email, password) {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  }

  return fetch(`/users/login`, requestOptions)
    .then(handleResponse)
    .then(user => {
      // login successful if there's a user in the response
      if (user) {
        console.log(user)
        // store user details and basic auth credentials in local storage
        // to keep user logged in between page refreshes
        user.authdata = window.btoa(email + ':' + password)
        console.log(JSON.stringify(user))
        console.log(user['token'])
        localStorage.setItem('user', JSON.stringify(user))
      }

      return user
    })
}

function register (firstName, lastName, email, password) {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ firstName, lastName, email, password })
  }

  return fetch(`/users/register`, requestOptions)
    .then(handleResponse)
    .then(user => {
      // registration successful if there's a user in the response
      if (user) {
      }

      return user
    })
}

function updateProfile (firstName, lastName, email, password) {
  const local = localStorage.user
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json',
      'token': JSON.parse(local).token},
    body: JSON.stringify({ firstName, lastName, email, password })
  }

  return fetch(`/users/updateProfile`, requestOptions)
    .then(handleResponse)
    .then(user => {
      // registration successful if there's a user in the response
      if (user) {
      }

      return user
    })
}

function getProfileInformation () {
  const local = localStorage.user
  console.log(JSON.parse(local).token)
  const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json',
      'token': JSON.parse(local).token}
  }

  return fetch(`/users/getProfileInformation`, requestOptions)
    .then(handleResponse)
    .then(user => {
      console.log(user)
      // registration successful if there's a user in the response
      if (user) {
      }

      return user
    })
}

function uploadUserProfileImage (file) {
  const local = localStorage.user
  console.log(JSON.parse(local).token)
  const formData = new FormData()
  formData.append('photo', file, file.name)
  console.log(file)
  console.log(file.name)
  console.log(formData)
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'multipart/form-data',
      'token': JSON.parse(local).token}
  }
  console.log(requestOptions)
  return fetch(`/users/profileImage/upload`, formData, requestOptions)
    .then(handleResponse)
    .then(user => {
      console.log(user)
      // registration successful if there's a user in the response
      if (user) {
      }

      return user
    })
}

function logout () {
  // remove user from local storage to log user out
  localStorage.removeItem('user')
}

function getAll () {
  const requestOptions = {
    method: 'GET',
    headers: authHeader()
  }
  return fetch(`/users`, requestOptions).then(handleResponse)
}

function handleResponse (response) {
  return response.text().then(text => {
    const data = text && JSON.parse(text)
    console.log(response)
    console.log(JSON.parse(text))
    console.log(response.status)
    console.log(data)
    console.log('55 atleasrt i am here')
    if (!response.ok) {
      if (response.status === 401) {
        console.log('66getting kickedout atleasrt i am here')
        // auto logout if 401 response returned from api
        logout()
        location.reload(true)
      }

      const error = (data && data.error) || response.statusText
      return Promise.reject(error)
    }

    return data

    // return Promise.reject(data['error'])
  })
}
