import streamlit as st
from routh_hurwitz import (
    display_table,
    display_polynomial,
    generate_table,
    get_polynomial,
)

st.set_page_config(
    page_title='Routh-Hurwitz Table Generator',
    page_icon='https://github.com/alvii147/RouthHurwitz/raw/main/img/logo.svg',
    layout='wide',
)

_, col1, _, col2, _ = st.columns([1, 3, 1, 1, 1])

with col1:
    st.header('Routh-Hurwitz Table Generator', divider=True)
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
        'logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBI'
        'WXMAAAXnAAAF5wGk6LX5AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAq1JREF'
        'UWIXtljtoVEEUhr+ZO/ex2btrEslutBFEVBS0tlIRxc7GWkTwWYmNjya1jaD4SCMidpJKREQJIhY2Io'
        'pgI0Qb4yYkWZPsbrL3McfiKiq+9ppIEDLNnRn++c93hzNzRokIS9n0kkZfBlgGAMxfrRo+sRad7sNxt'
        'iJKSJOXiHOHXVdH8lqpXMfwydFVpOYWxtkiYbFHPM8AqChKVLNRJ7UvsBxgx5Xa4gMMH1mPcR/Zlb2r'
        'KBTUTzVzLdGTU6NEdie7B98sHsDdo12E5rXtr6zBdUEsqtmCKAIBfA8pFkEpiCL02Pg7/GAT2y7M/cm'
        '6syQM9TlZUa7iuhDHqIkp1OQkanYW1ZjN+hMTEMfgedhyuZ/51plOrDsDUByUUhgAWdBW80dJq4Wamc'
        'kG5VKAVocWB2D4cBXXNdn2tlGNxq85m01ot0EpxDEeD45XFg7gmD7ROtM5DvwuZ0QyDaCMAY9FAIj0t'
        'EqtBSBO/ignSbOvTQVLfeEATyvvSdIs24MAKXb9UipdRQj8bCfiVHjS/2HhAAMDFpH7tJrZr4Ul8Lwf'
        'da4HYZj1W80U7D0GBuzCAQDS+LSq1ydJLRIE2EofUgrB98H3kVKIrVaQQgBpiq5PT6DbHR3Dzm/Cx8d'
        '2o8xtW610Yz6XkC9Lv9yLSYKujX/EJvvZOTjciW3n1XD74MPohRpUIzXU2BS0o88EkvXHplAjNZJXzr'
        'VOg0POaijv3bfRqMH2NrDVcdxuDwTi6Qhd60LXCyDqXR7T/OVYIBmFseej301X+9fh+bnd/tcHCaC1l'
        'qBQfgAwPzezh6+pmM/nL9bE2pibhZ7ezauvD+1dfX1ob8kvb9DGvQgyn9cs1w5okWfWURuL5y+PFL+Z'
        '77sx9AY42T576pJOpTuPZ74n2T9oS56EywDLAJ8AW+cNFMG2irIAAAAASUVORK5CYII=&'
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
        'logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAIGNI'
        'Uk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAKXUExURQAAAGBgYBERERYWFgU'
        'FBRUVFQ8PD1JSUicnJwkJCSMjIx0dHTY2NgICAjExMRoaGtsZPH8hMqIAFx8fH9sfQd0tTS8ABDAwMN'
        'xBXdcAHtgCKHFxcdoPNNkILhISEtoUOBgYGNgFKwYGBtgEK3CnSNoTNnmsVNkNMtkILXKoSnWqT9s+W'
        '9cAH9gBKG6mRWeiPKHCht0sTIR7OWmjP4e0Z3+wXdoYO61lTL0iKH6vWnutV3ytV4q2am6lRYKxX2eh'
        'PHKoS4CwXZ7EiHaqUHmsU5vCgDQ0NAoKCgYGBgMDAwICAgICAgEBAQMDAwQEBAsLCzc3Nzo6OggICAQ'
        'EBAICAgAAAAwMDAQEBAEBAQYJCAMDAwICAggICHMKHQsCBAICAggICNsHLtACJ9kKL9gCKd0zUtgEKg'
        'UFBUBAQNkILdgBKAkJCd0zUdgEKgAAAAAAANkKMNgCKI+Pj7y8vNkGLNgAJ/Pz8/Hx8dgEK/Dw8NgDK'
        'fDw8NgCKfDw8NgBKPDw8PLx8vDw8LvSqtTgy22lRFubLdkHLW6lRXKoSt0vT2+mR4y3bdgCKW6mRnOp'
        'TNoFLdQIKm6mRXKoSqZXPHKfRHGnSXGqS3GoSnOpTW+mR26lRXOoTHGoSm+mR26lRW2lRG6mRW+mR4u'
        '2bIq2anKoS3CnSG+mR26mRm6mRW6lRXOoTIy3bAAAAGwAFAUAAdkAJ9MAJtgAJwYAAdEAJJIlOYR/gI'
        'aHh4aGhtwJL+h8j/Pu7/T19fT09NgAJtkGLOR4i+/q6/Dx8fDw8NkFLNgFK+R6jvDt7uR7jtoHLuZ5j'
        'vLs7vLy9PLx89UDJ7deULXJn7bQpbbPpNYEKKNTNXChRGylQ2ykQmykQ2+hQ2ymRG2lRKNTNv///6rK'
        'Eb0AAACsdFJOUwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAACK2+w3PT+3LArAgI5muH8GozsN8TEN0Pb20M32xrFAoyMAjnsOQ'
        'KamgIr4eAqb/z8bK+t3Nr08v79/GzgKpoCOes5AosCxMQaN9vbN0PbQzY3GozsGjmZ4fzhmgICK2+v3'
        'PT+KwK/OOV3AAAAAWJLR0TcB2CDtwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB+gEDhEoH+4t'
        'iKQAAAG1SURBVDjLY2AAAUYmZhY3dw9PL28fH29fPw//ABZWNnYGOOBg4AwMCg4JXQMFoSHBQQGcDFw'
        'weW4e3rDwiDUoICI8jJePHyIvICgUGbUGA0THMAiDVYiIisXGrcEC4hMYxIG2SEhKJSatXYdVRQwvgz'
        'SDjGxyyvoN2FVEhXHKMcinpm3ciEtFeoYCg2Jm1kacKiKylRhycjduhKjYhEVFXj5DQeFGiIrNW7Zu2'
        '44OiooZSko3QsGOnbt270EDZeUMFTD5jXv37T9w8BAaqGSo2ohQcRhTRTVDzUa8KmoZ6jYiqzhy9Biq'
        'gnp0BccxFKBYsQ+LFVV45YGOJOhNeEDtPXHy1OkzaKChERHUZ8+dv3ARHTQ1M6RCI+vS5StXr6GD6y2'
        'tDMptWRD5GzdvYYD2DhUG1c40nPK3urrVGNQ1kns24pDv7dPUYtDW0e2fcBur/MRJevoGwGRvaDR5Cl'
        'b5qcYmpqCMYWZuMa0Xi/nTjS2tIFnL2kZvxsxZqNKzZs62NbGCZU47e4fuOXPnzYfJzl+wsGORpr0jI'
        'ns7OaupLF6ydNnyFStXrli+bOmq1SouWq5gKQBRdGzLoG9/PwAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAy'
        'NC0wNC0xNFQxNzo0MDoyOSswMDowMG3aqdYAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjQtMDQtMTRUMTc'
        '6NDA6MjkrMDA6MDAchxFqAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDI0LTA0LTE0VDE3OjQwOjMxKz'
        'AwOjAwtNd+TAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII=&'
        'style=for-the-badge'
    )
    pcrf_url = 'https://www.pcrf.net'

    st.write(f'[![GitHub Stars]({github_shields_url})]({github_url})')
    st.write(f'[![License]({license_shields_url})]({license_url})')
    st.write(f'[![LinkedIn]({linkedin_shields_url})]({linkedin_url})')
    st.write(f'[![PCRF]({pcrf_shields_url})]({pcrf_url})')
