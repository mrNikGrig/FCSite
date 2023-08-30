//const counters = document.querySelectorAll('[data-counter]');
//let counterGlobal = 1;
//
//
//if (counters) {
//	counters.forEach(counter => {
//		counter.addEventListener('click', e => {
//			const target = e.target;
//
//			if (target.closest('.counter__button')) {
//				if (target.closest('.counter').querySelector('input').value == '' && (target.classList.contains('counter__button_minus') || target.classList.contains('counter__button_plus'))) {
//					target.closest('.counter').querySelector('input').value = 1;
//				}
//
//				let counter = parseInt(target.closest('.counter').querySelector('input').value);
//
//				if (target.classList.contains('counter__button_plus')) {
//					counter++;
//				} else {
//					--counter;
//				}
//
//				if (counter <= 0) {
//					counter = 0;
//					target.closest('.counter').querySelector('.counter__button_minus').classList.add('disabled')
//				} else {
//					target.closest('.counter').querySelector('.counter__button_minus').classList.remove('disabled')
//				}
//				target.closest('.counter').querySelector('input').value = counter;
//				window.quantity = {
//                  quantityVar: counter
//
//                };
//                counterGlobal = counter;
//			}
//		})
//	})
//}
//
//function button_click(button) {
//// button.name counterGlobal
//        document.cookie = "name=" + encodeURIComponent(button.name);
//        document.cookie = "quality=" + encodeURIComponent(counterGlobal);
//        alert(document.cookie)
//    }
