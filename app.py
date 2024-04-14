import streamlit as st
from routh_hurwitz import (
    display_table,
    display_polynomial,
    generate_table,
    get_polynomial,
)

st.set_page_config(
    page_title='Routh-Hurwitz Table Generator',
    layout='wide',
)

_, col1, _, col2, _ = st.columns([1, 3, 1, 1, 1])

with col1:
    st.write('# Routh-Hurwitz Table Generator')
    st.write('### Polynomial')

    polynomial_coeffs = st.text_input(
        label='Enter polynomial coefficients separated by commas',
        key='polynomial_coeffs',
        placeholder='1,a**2,3',
    )

    if polynomial_coeffs:
        st.latex(
            display_polynomial(
                get_polynomial(
                    st.session_state.polynomial_coeffs.split(','),
                ),
            ),
        )

    button_clicked = st.button(
        label='Go',
        key='go',
    )

    if polynomial_coeffs and button_clicked:
        st.write('### Routh-Hurwitz Table')

        st.markdown(
            display_table(
                generate_table(
                    st.session_state.polynomial_coeffs.split(',')
                ),
            ),
            unsafe_allow_html=True,
        )

with col2:
    wikipedia_link = (
        'https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_stability_criterion'
    )

    st.write('#### Routh-Hurwitz Stability Criterion')
    st.write(
        f'The [Routh-Hurwitz Stability Criterion]({wikipedia_link}) states that '
        'any system can be stable if and only if all the roots of the second '
        'column have the same sign. The number of sign changes in the second '
        'column of the Routh-Hurwitz table is equal to the number of roots of '
        'the characteristic equation in the closed right half of the complex '
        'plane.'
    )

    github_shields_url = (
        'https://img.shields.io/github/stars/alvii147/RouthHurwitz?'
        'logo=github&'
        'style=for-the-badge&'
        'color=181717'
    )
    github_url = 'https://github.com/alvii147/RouthHurwitz'

    license_shields_url = (
        'https://img.shields.io/github/license/alvii147/RouthHurwitz?'
        'style=for-the-badge'
    )
    license_url = 'https://github.com/alvii147/RouthHurwitz/blob/main/LICENSE'

    linkedin_shields_url = (
        'https://img.shields.io/badge/LinkedIn-0A66C2?'
        'logo=linkedin&'
        'style=for-the-badge'
    )
    linkedin_url = 'https://www.linkedin.com/in/zahin-zaman'

    pcrf_shields_url = (
        'https://img.shields.io/badge/Palestinian%20Children%27s%20Relief%20Fund-A60001?'
        'style=for-the-badge'
    )
    pcrf_url = 'https://www.pcrf.net'

    st.write(f'[![GitHub Stars]({github_shields_url})]({github_url})')
    st.write(f'[![License]({license_shields_url})]({license_url})')
    st.write(f'[![LinkedIn]({linkedin_shields_url})]({linkedin_url})')
    st.write(f'[![PCRF]({pcrf_shields_url})]({pcrf_url})')
