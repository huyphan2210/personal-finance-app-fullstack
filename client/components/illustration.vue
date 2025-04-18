<template>
  <aside class="topbar">
    <SharedLogo class="logo" />
  </aside>
  <aside class="sidebar">
    <SharedLogo class="logo" />
    <article class="sidebar_content">
      <picture class="sidebar_content_illustration">
        <img src="../assets/images/illustration-authentication.svg" loading="lazy" alt="Login Illustration" />
      </picture>
      <div class="sidebar_content_text">
        <p>
          Keep track of your money
          and save for your future
        </p>
        <p>
          Personal finance app puts you in control of your spending. Track transactions, set budgets, and add to savings
          pots easily.
        </p>
      </div>
    </article>
  </aside>
</template>

<style lang="scss" scoped>
.topbar {
  order: 1;
  background-color: var(--grey-900);
  text-align: center;
  padding: 2.5rem;
  border-radius: 0 0 0.5rem 0.5rem;
}

.sidebar {
  display: none;
  padding: 1.25rem;
  background-color: var(--white);
  width: 40%;
  max-width: 35rem;
  max-height: calc(100vh - 2.5rem);
  position: relative;

  .logo {
    position: absolute;
    top: 3.75rem;
    left: 3.75rem;
  }

  &_content {
    background-color: var(--grey-900);
    border-radius: 0.75rem;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    &_illustration {
      align-self: flex-start;
      max-height: 700px;
      overflow: hidden;

      img {
        width: 100%;
      }
    }

    &_text {
      padding: 2.5rem;

      p {
        color: var(--white);
        font-size: 0.875rem;
        line-height: 1.5;

        &:first-child {
          font-size: 2rem;
          font-weight: 700;
          margin-bottom: 1.5rem;
          line-height: 1.2;
        }
      }
    }
  }
}

@media screen and (min-width: 64rem) {
  .topbar {
    display: none;
  }

  .sidebar {
    display: flex;
  }
}
</style>
